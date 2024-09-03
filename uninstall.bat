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



@REM run as admin
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo =========================================================================
echo.
echo   ABUS Uninstaller [Version 3.0]
echo   contact: abus.aikorea@gmail.com
echo.
echo =========================================================================
echo.

:: If we've reached here, we're running in the correct environment
:: Your actual batch file commands start here
echo Running in 64-bit mode from System32
echo Current directory: %CD%
echo Command line: %*


cd /D "%~dp0"


:: quit task
choice /C YN /N /T 10 /D Y /M "Terminate all running python.exe. Do you want to continue (Y/N)?"
if errorlevel 2 (
    echo.
    echo Quit Uninstallation. 
    pause
    exit 0
)
taskkill /f /im python.exe /t
echo.


echo.
choice /C NY /N /T 10 /D N /M "Would you like to remove system packages (not recommended) (N/Y)?"
if errorlevel 2 (
    echo.
    echo Start Uninstallation. 

    :: Uninstall packages
    choco uninstall -y git.install
    choco uninstall -y ffmpeg
    @REM choco uninstall -y cuda --version=11.8.0.52206
    @REM choco uninstall -y cuda --version=12.3.2.546
    choco uninstall -y cuda
    choco uninstall -y visualstudio2022-workload-vctools
    choco uninstall -y visualstudio2022buildtools
)


:: remove folder
if exist "%~dp0\installer_files\" (
    echo Deleting installer_files folder ...
    echo Please wait a moment

    rmdir /s /q "%~dp0\installer_files"
) 
echo ABUS uninstall.bat finished.
pause

:: Rebooting
for /l %%i in (30,-1,1) do (
    cls
    echo.    
    echo ABUS Uninstaller finished.
    echo System will be rebooted in %%i seconds.
    timeout /t 1 /nobreak >nul
)
shutdown /r /t 0