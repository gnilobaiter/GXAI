@echo off
set VENV_DIR=%~dp0.venv

if not exist "%VENV_DIR%\Scripts\activate" (
    echo -------------------------------------------------------
    echo ---      !!! Virtual environment not found !!!      ---
    echo ---!!! Please run install.bat first to set it up.!!!---
    echo -------------------------------------------------------
    pause
    exit /b
)

call "%VENV_DIR%\Scripts\activate"

echo Starting the application...
python ./src/app.py %*

pause