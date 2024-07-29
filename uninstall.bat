@echo off
setlocal enabledelayedexpansion

@REM run as admin
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

echo =========================================================================
echo.
echo   ABUS Uninstaller [Version 3.0]
echo   contact: abus.aikorea@gmail.com
echo.
echo =========================================================================
echo.

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