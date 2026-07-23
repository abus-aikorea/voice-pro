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



echo =========================================================================
echo.
echo   ABUS Launcher [Version 4.0 - uv]
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
set PATH=%PATH%;%SystemRoot%\system32


:: Check for special characters in installation path
set "SPCHARMESSAGE="WARNING: Special characters were detected in the installation path!" "         This can cause the installation to fail!""
echo "%CD%"| findstr /R /C:"[!#\$%&()\*+,;<=>?@\[\]\^`{|}~]" >nul && (
	call :PrintBigMessage %SPCHARMESSAGE%
)
set SPCHARMESSAGE=


:: fix failed install when installing to a separate drive
set TMP=%cd%\installer_files
set TEMP=%cd%\installer_files


:: config
set INSTALL_DIR=%cd%\installer_files
set INSTALL_ENV_DIR=%cd%\installer_files\env
set UV_VERSION=0.11.28
set UV_DIR=%INSTALL_DIR%\uv
set UV_EXE=%UV_DIR%\uv.exe

if not exist "%INSTALL_DIR%" (
	mkdir "%INSTALL_DIR%" 2>nul || ( echo. && echo Cannot create "%INSTALL_DIR%". Check folder permissions. && goto end )
)

call :CheckWritable "%INSTALL_DIR%" || goto end
if exist "%INSTALL_ENV_DIR%" (
	call :CheckWritable "%INSTALL_ENV_DIR%" || goto end
)

:: keep everything project-local (no global uv/python/cache pollution)
set UV_PYTHON_INSTALL_DIR=%INSTALL_DIR%\python
set UV_CACHE_DIR=%INSTALL_DIR%\uv-cache
set UV_PROJECT_ENVIRONMENT=%INSTALL_ENV_DIR%

:: environment isolation
set PYTHONNOUSERSITE=1
set PYTHONPATH=
set PYTHONHOME=


:: (if necessary) download uv into a contained folder
:: NOTE: extraction must use the built-in bsdtar with its full path. A bare `tar` may
:: resolve to GNU tar from Git which cannot read zip files, and PowerShell
:: Expand-Archive may be blocked by group policy on corporate machines.
if not exist "%UV_EXE%" (
	echo Downloading uv %UV_VERSION% to %UV_DIR%
	mkdir "%UV_DIR%" 2>nul
	call curl -Lk "https://github.com/astral-sh/uv/releases/download/%UV_VERSION%/uv-x86_64-pc-windows-msvc.zip" -o "%INSTALL_DIR%\uv.zip" || ( echo. && echo uv failed to download. && goto end )
	"%SystemRoot%\System32\tar.exe" -xf "%INSTALL_DIR%\uv.zip" -C "%UV_DIR%" || ( echo. && echo uv failed to extract. && goto end )
	del "%INSTALL_DIR%\uv.zip"
)

:: test the uv binary
echo uv version:
call "%UV_EXE%" --version || ( echo. && echo uv not found. && goto end )


:: (if necessary) provide a portable ffmpeg - needed for downloads, transcription and
:: media processing. Uses a project-local copy when ffmpeg is not on PATH, so no
:: administrator rights are required (configure.bat/choco stays optional).
set "FFMPEG_DIR=%INSTALL_DIR%\ffmpeg"
where ffmpeg >nul 2>&1
if errorlevel 1 (
	if not exist "%FFMPEG_DIR%\bin\ffmpeg.exe" (
		echo ffmpeg not found - downloading a portable copy to %FFMPEG_DIR%
		call curl -Lk "https://github.com/BtbN/FFmpeg-Builds/releases/latest/download/ffmpeg-master-latest-win64-gpl.zip" -o "%INSTALL_DIR%\ffmpeg.zip" || ( echo. && echo ffmpeg failed to download. && goto end )
		mkdir "%FFMPEG_DIR%" 2>nul
		"%SystemRoot%\System32\tar.exe" -xf "%INSTALL_DIR%\ffmpeg.zip" -C "%FFMPEG_DIR%" --strip-components=1 || ( echo. && echo ffmpeg failed to extract. && goto end )
		del "%INSTALL_DIR%\ffmpeg.zip"
	)
)
if exist "%FFMPEG_DIR%\bin\ffmpeg.exe" set "PATH=%FFMPEG_DIR%\bin;%PATH%"


:: figure out the GPU choice: GPU_CHOICE env var > saved choice > NVIDIA registry autodetect
set SAVED_CHOICE_FILE=%INSTALL_DIR%\gpu_choice.txt
if not defined GPU_CHOICE (
	if exist "%SAVED_CHOICE_FILE%" (
		set /p GPU_CHOICE=<"%SAVED_CHOICE_FILE%"
	)
)
if not defined GPU_CHOICE (
	set GPU_CHOICE=C
	set "registry_path=HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000"
	for /f "tokens=2*" %%a in ('reg query "!registry_path!" /v "DriverDesc" 2^>nul ^| findstr /i /c:"DriverDesc"') do (
		set "value=%%b"
	)
	if not "!value!"=="" (
		echo "!value!" | findstr /I /C:"nvidia" >nul 2>&1 && set GPU_CHOICE=G
		echo "!value!" | findstr /I /C:"tesla" >nul 2>&1 && set GPU_CHOICE=G
	)
)
echo !GPU_CHOICE!>"%SAVED_CHOICE_FILE%"

if /i "!GPU_CHOICE!"=="G" (
	set SYNC_EXTRA=gpu
	echo GPU mode: NVIDIA ^(CUDA 12.8^)
) else (
	set SYNC_EXTRA=cpu
	echo GPU mode: CPU
)
echo To change this, delete "%SAVED_CHOICE_FILE%" or set the GPU_CHOICE environment variable ^(G=NVIDIA, C=CPU^).


:: install/update the environment from the committed lockfile (installs Python automatically)
call "%UV_EXE%" sync --frozen --extra !SYNC_EXTRA! || ( echo. && echo Environment installation failed. && goto end )


:: check if the environment was actually created
if not exist "%INSTALL_ENV_DIR%\Scripts\python.exe" ( echo. && echo Python environment is empty. && goto end )


set LOG_LEVEL=DEBUG
call "%INSTALL_ENV_DIR%\Scripts\python.exe" start-abus.py voice

:: below are functions for the script   next line skips these during normal execution
goto end


:PrintBigMessage
echo. && echo.
echo *******************************************************************
for %%M in (%*) do echo * %%~M
echo *******************************************************************
echo. && echo.
exit /b

:CheckWritable
set "CHECK_DIR=%~1"
set "WRITE_TEST=%CHECK_DIR%\.write-test-%RANDOM%.tmp"
> "%WRITE_TEST%" echo writable 2>nul
if errorlevel 1 (
	echo.
	echo "%CHECK_DIR%" is not writable by the current user.
	echo If a previous install was run as Administrator, restore folder ownership or delete installer_files and run start.bat again.
	exit /b 1
)
del "%WRITE_TEST%" >nul 2>&1
exit /b 0

:end
pause
