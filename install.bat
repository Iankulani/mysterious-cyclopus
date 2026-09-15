@echo off
REM ============================================================
REM  🐙 MYSTERIOUS CYCLOPUS - Windows Batch Installer
REM ============================================================
setlocal EnableDelayedExpansion
title Mysterious Cyclopus - Installer

set "PROJECT_DIR=%~dp0"
set "VENV_DIR=%PROJECT_DIR%.venv"
set "PYTHON_BIN=python"

echo.
echo    __  ___               __                        __
echo   /  ^|/  /_  _____  ___ / /____ ___   ___  ___ ___/ /  __ __ ___
echo  / /^|_/ / / / / _ \/ _ / __/ -_) _ \ / _ \/ -_) _  /  / // /(_-^<
echo /_/  /_/_/ /_/\___/_/ /_/\__/\___/ /_//_/\__/\_,_/   \_,_//___/
echo.
echo         🐙 MYSTERIOUS CYCLOPUS v1.0.0 - Installer 🐙
echo ============================================================
echo.

REM --- Check Python ---
echo [*] Checking Python...
where %PYTHON_BIN% >nul 2>nul
if errorlevel 1 (
    echo [X] Python not found in PATH. Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('%PYTHON_BIN% --version 2^>^&1') do set PYVER=%%v
echo [✓] Python %PYVER% detected.
echo.

REM --- Check pip ---
echo [*] Checking pip...
%PYTHON_BIN% -m pip --version >nul 2>nul
if errorlevel 1 (
    echo [!] pip not found. Attempting to install...
    %PYTHON_BIN% -m ensurepip --upgrade
)

REM --- Create venv ---
echo [*] Creating virtual environment...
if not exist "%VENV_DIR%" (
    %PYTHON_BIN% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo [X] Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo [✓] Virtual environment created.
) else (
    echo [!] Virtual environment already exists.
)

REM --- Activate venv ---
call "%VENV_DIR%\Scripts\activate.bat"
echo [✓] Virtual environment activated.

REM --- Upgrade pip ---
echo [*] Upgrading pip / setuptools / wheel...
python -m pip install --upgrade pip setuptools wheel

REM --- Install requirements ---
echo [*] Installing Python requirements...
if exist "%PROJECT_DIR%requirements.txt" (
    pip install -r "%PROJECT_DIR%requirements.txt"
    if errorlevel 1 (
        echo [!] Some packages failed to install - continuing.
    )
) else (
    echo [X] requirements.txt not found.
    pause
    exit /b 1
)

REM --- Optional: install Nmap / Wireshark via winget ---
echo.
set /p INSTALL_TOOLS="Install Nmap & Wireshark via winget? (y/n): "
if /i "%INSTALL_TOOLS%"=="y" (
    where winget >nul 2>nul
    if errorlevel 1 (
        echo [!] winget not available - skipping.
    ) else (
        echo [*] Installing Nmap...
        winget install -e --id Insecure.Nmap --accept-source-agreements --accept-package-agreements
        echo [*] Installing Wireshark...
        winget install -e --id Wireshark.Wireshark --accept-source-agreements --accept-package-agreements
    )
)

REM --- Run self check ---
echo.
echo [*] Running requirements checker...
if exist "%PROJECT_DIR%requirements-check.py" (
    python "%PROJECT_DIR%requirements-check.py" -v
)

REM --- Create launcher ---
echo [*] Creating launcher...
(
    echo @echo off
    echo cd /d "%PROJECT_DIR%"
    echo call "%VENV_DIR%\Scripts\activate.bat"
    echo python "%PROJECT_DIR%mysterious_cyclopus.py" %%*
) > "%PROJECT_DIR%run.bat"
echo [✓] Launcher created: run.bat

echo.
echo ============================================================
echo [✓] Installation complete!
echo ============================================================
echo To run:
echo    run.bat
echo or:
echo    .venv\Scripts\activate
echo    python mysterious_cyclopus.py
echo.
pause
endlocal