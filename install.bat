@echo off

git pull

set VENV_DIR=%~dp0.venv

mkdir tmp 2>NUL

python -m venv "%VENV_DIR%"
if %ERRORLEVEL% neq 0 (
    echo Unable to create venv
    pause
    exit /b
)

if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo Creating venv in directory %VENV_DIR%
    python -m venv "%VENV_DIR%"
    if %ERRORLEVEL% neq 0 (
        echo Unable to create venv
        pause
        exit /b
    )
)

set PYTHON=%VENV_DIR%\Scripts\python.exe

call "%VENV_DIR%\Scripts\activate"

echo Installing pip:
python -m pip install pip==24.0
echo Installing pip-tools:
python -m pip install pip-tools
if not exist requirements.txt (
    echo Compiling requirements:
    python -m piptools compile requirements.in
) else (
    echo --------------------------------------------------------------------
    echo ---!!! requirements.txt already exists, skipping compilation. !!!---
    echo ------!!! IF YOU WANT RECOMPILE, DELETE requirements.txt  !!!-------
    echo --------------------------------------------------------------------
)

echo Installing requirements:
python -m pip install -r requirements.txt

echo Running run.bat:
call run.bat

pause