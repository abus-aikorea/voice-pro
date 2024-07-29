@echo off
setlocal enabledelayedexpansion

:: run as admin
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo =========================================================================
echo.
echo   ABUS Configure [Version 3.0]
echo   contact: abus.aikorea@gmail.com
echo.
echo =========================================================================
echo.


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