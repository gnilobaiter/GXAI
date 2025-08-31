@echo off

git pull

set PYTHON=py -3.10
set VENV_DIR=%~dp0venv

mkdir tmp 2>NUL

%PYTHON% -m venv "%VENV_DIR%"
if %ERRORLEVEL% neq 0 (
    echo Unable to create venv
    pause
    exit /b
)

if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo Creating venv in directory %VENV_DIR%
    %PYTHON% -m venv "%VENV_DIR%"
    if %ERRORLEVEL% neq 0 (
        echo Unable to create venv
        pause
        exit /b
    )
)

set PYTHON=%VENV_DIR%\Scripts\python.exe

call "%VENV_DIR%\Scripts\activate"

echo Installing pip:
%PYTHON% -m pip install pip==24.0
echo Installing pip-tools:
%PYTHON% -m pip install pip-tools
if not exist requirements.txt (
    echo Compiling requirements:
    %PYTHON% -m piptools compile requirements.in
) else (
    echo --------------------------------------------------------------------
    echo ---!!! requirements.txt already exists, skipping compilation. !!!---
    echo ------!!! IF YOU WANT RECOMPILE, DELETE requirements.txt  !!!-------
    echo --------------------------------------------------------------------
)

echo Installing requirements:
%PYTHON% -m pip install -r requirements.txt
echo Installing torch:
%PYTHON% -m pip install torch torchvision==0.16.2 torchaudio --index-url https://download.pytorch.org/whl/cu121

echo Running run.bat:
call run.bat

pause