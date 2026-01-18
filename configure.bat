@echo off
setlocal enabledelayedexpansion


:: Check if we're running in SysWOW64
if /i "%PROCESSOR_ARCHITECTURE%"=="x86" (
    if defined PROCESSOR_ARCHITEW6432 (
        :: We're running in 32-bit mode on a 64-bit system
        :: Re-launch using 64-bit cmd.exe
        %SystemRoot%\Sysnative\cmd.exe /c "%~dpnx0" %*
        exit /b
    )
)

:: At this point, we're running in 64-bit mode
:: Check if the script is being run directly or through another cmd instance
if /i "%~dp0"=="%SystemRoot%\SysWOW64\" (
    :: We're running from SysWOW64, re-launch using System32 cmd.exe
    %SystemRoot%\System32\cmd.exe /c "%~dpnx0" %*
    exit /b
)



:: run as admin
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo =========================================================================
echo.
echo   ABUS Configure [Version 3.0]
echo   contact: abus.aikorea@gmail.com
echo.
echo =========================================================================
echo.

:: If we've reached here, we're running in the correct environment
:: Your actual batch file commands start here
echo Running in 64-bit mode from System32
echo Current directory: %CD%
echo Command line: %*


:: check LongPathsEnabled
echo Enabling long paths support...
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f
if %ERRORLEVEL% == 0 (
    echo Long paths have been enabled successfully.
) else (
    echo Failed to enable long paths.
    pause
    exit /b 1
)



cd /D "%~dp0"
SET "CHOCPATH=%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe"

:: Install choco
echo Checking Chocolatey installation...
where choco >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Chocolatey...
    %CHOCPATH% -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install Chocolatey.
        pause
        exit /b 1
    )
    :: Add Chocolatey to PATH for current session
    if exist "%ALLUSERSPROFILE%\chocolatey\bin" (
        set "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    )
    :: Verify choco is now available
    where choco >nul 2>&1
    if %errorlevel% neq 0 (
        echo WARNING: Chocolatey installed but choco command not found in PATH.
        echo You may need to restart the command prompt.
    )
) else (
    echo Chocolatey is already installed.
)

:: Install uv
@REM %CHOCPATH% -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


:: check NVIDIA GPU - check all GPU entries, not just 0000
set IS_NVIDIA_GPU=0
set "registry_base=HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}"
set "search_key=DriverDesc"

:: Loop through all GPU entries (0000-0099) - most systems won't have more than 10 GPUs
for /l %%i in (0,1,99) do (
    :: Format entry number with leading zeros using string manipulation
    set "num=0000%%i"
    set "num=!num:~-4!"
    set "registry_path=!registry_base!\!num!"
    
    set "value="
    for /f "tokens=2*" %%a in ('reg query "!registry_path!" /v "%search_key%" 2^>nul ^| findstr /i /c:"%search_key%"') do (
        set "value=%%b"
    )
    
    if not "!value!"=="" (
        echo Checking GPU %%i: DriverDesc is "!value!"
        set "substring=nvidia"
        echo "!value!" | findstr /I /C:"!substring!" >nul 2>&1
        if !errorlevel! equ 0 (
            echo NVIDIA GPU found at entry %%i
            set IS_NVIDIA_GPU=1
            goto :nvidia_found
        ) else (
            set "substring=tesla"
            echo "!value!" | findstr /I /C:"!substring!" >nul 2>&1
            if !errorlevel! equ 0 (
                echo TESLA GPU found at entry %%i
                set IS_NVIDIA_GPU=1
                goto :nvidia_found
            )
        )
    )
)

:nvidia_found

:: install CUDA
if !IS_NVIDIA_GPU! equ 1 (
    echo.
    echo =========================================================================
    echo NVIDIA GPU detected - Installing CUDA
    echo =========================================================================
    echo.
    echo CUDA 12.3.2 requires NVIDIA driver version 525.60.13 or higher.
    echo If installation fails, please update your NVIDIA driver first.
    echo.
    @REM choco install -y cuda --version=11.8.0.52206
    choco install -y cuda --version=12.3.2.546
    if %errorlevel% neq 0 (
        echo.
        echo WARNING: CUDA installation failed.
        echo Possible reasons:
        echo 1. NVIDIA driver version is too old
        echo 2. Another CUDA version is already installed
        echo 3. Insufficient disk space
        echo.
        echo Continuing with other installations...
        echo.
    ) else (
        echo CUDA installed successfully.
    )
) else (
    echo NVIDIA or TESLA GPU is not found
    echo Skipping CUDA installation.
    echo.
)

echo.
echo =========================================================================
echo Installing required packages...
echo =========================================================================
echo.

echo Installing git.install...
choco install -y git.install
if %errorlevel% neq 0 (
    echo WARNING: git.install installation failed.
)

echo.
echo Installing ffmpeg...
choco install -y ffmpeg
if %errorlevel% neq 0 (
    echo WARNING: ffmpeg installation failed.
)

echo.
echo Installing Visual Studio 2022 Build Tools...
echo This may take a very long time (30+ minutes)...
choco install -y visualstudio2022buildtools --verbose
if %errorlevel% neq 0 (
    echo WARNING: visualstudio2022buildtools installation failed.
)

echo.
echo Installing Visual Studio 2022 C++ workload...
choco install -y visualstudio2022-workload-vctools --verbose
if %errorlevel% neq 0 (
    echo WARNING: visualstudio2022-workload-vctools installation failed.
)

echo.
echo =========================================================================
echo ABUS configure.bat finished.
echo =========================================================================
echo.
echo Note: LongPathsEnabled requires a system reboot to take effect.
echo.

:: Ask user about reboot
set /p REBOOT_NOW="Do you want to reboot now? (Y/N): "
if /i "!REBOOT_NOW!"=="Y" (
    echo.
    echo System will be rebooted in 30 seconds...
    echo Press Ctrl+C to cancel.
    echo.
    for /l %%i in (30,-1,1) do (
        cls
        echo.
        echo =========================================================================
        echo ABUS Configure finished.
        echo =========================================================================
        echo.
        echo System will be rebooted in %%i seconds.
        echo Press Ctrl+C to cancel.
        timeout /t 1 /nobreak >nul 2>&1
    )
    shutdown /r /t 0
) else (
    echo.
    echo Please reboot your system manually when ready.
    echo LongPathsEnabled and CUDA changes require a reboot to take effect.
    pause
)
