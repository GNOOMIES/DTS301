@echo off
echo ==========================================
echo   DTS301 Python Environment Setup
echo ==========================================

:: 1. Check that Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo and tick "Add python.exe to PATH" during installation.
    pause
    exit /b 1
)

:: 2. Create virtual environment (.venv) if it doesn't exist
if not exist ".venv" (
    echo [1/4] Creating virtual environment (.venv)...
    python -m venv .venv
) else (
    echo [1/4] Virtual environment (.venv) already exists.
)

:: 3. Upgrade pip and install requirements
echo [2/4] Upgrading pip...
.venv\Scripts\python.exe -m pip install --upgrade pip

echo [3/4] Installing Python packages from requirements.txt...
.venv\Scripts\pip.exe install -r requirements.txt

:: 4. Install recommended VS Code extensions (if VS Code CLI is available)
where code >nul 2>&1
if %errorlevel% equ 0 (
    echo [4/4] Installing VS Code extensions...
    call code --install-extension ms-python.python
    call code --install-extension ms-toolsai.jupyter
    call code --install-extension ms-python.black-formatter
) else (
    echo [4/4] VS Code CLI not found in PATH - skipping automatic extension install.
)

echo.
echo ==========================================
echo   Setup Complete!
echo   In VS Code: Press Ctrl+Shift+P, search
echo   "Python: Select Interpreter", and pick .venv
echo ==========================================
pause