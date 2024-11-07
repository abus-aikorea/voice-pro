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


:: LongPathsEnabled 값 설정
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
%CHOCPATH% -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"


:: check NVIDIA GPU
set IS_NVIDIA_GPU=0
set "registry_path=HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000"
set "search_key=DriverDesc"
for /f "tokens=2*" %%a in ('reg query "%registry_path%" /v "%search_key%" 2^>nul ^| findstr /i /c:"%search_key%"') do (
    set "value=%%b"
)

if not "!value!"=="" (
    echo DriverDesc is "!value!"
    set "substring=nvidia"
    echo "!value!" | findstr /I /C:"!substring!" >nul 2>&1
    if !errorlevel! equ 0 (
        echo NVIDIA
        set IS_NVIDIA_GPU=1
    ) else (
        set "substring=tesla"
        echo "!value!" | findstr /I /C:"!substring!" >nul 2>&1
        if !errorlevel! equ 0 (
            echo TESLA
            set IS_NVIDIA_GPU=1
        )
    )
)

:: install CUDA
if !IS_NVIDIA_GPU! equ 1 (
    echo NVIDIA or TESLA GPU is found
    echo.
    @REM choco install -y cuda --version=11.8.0.52206
    choco install -y cuda --version=12.3.2.546
) else (
    echo NVIDIA or TESLA GPU is not found
    echo.
)

choco install -y git.install
choco install -y ffmpeg
choco install -y visualstudio2022buildtools --verbose
choco install -y visualstudio2022-workload-vctools --verbose


echo ABUS configure.bat finished.
pause

:: Rebooting
for /l %%i in (30,-1,1) do (
    cls
    echo.
    echo ABUS Configure finished.
    echo System will be rebooted in %%i seconds.
    timeout /t 1 /nobreak >nul
)
shutdown /r /t 0