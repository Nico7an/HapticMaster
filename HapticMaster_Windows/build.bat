@echo off

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo Erreur: Python n'est pas installé ou n'est pas dans le PATH
    pause
    exit /b 1
)

REM Installer les dépendances
echo.
echo [1/3] Installation des dépendances...
pip install -r requirements.txt

REM Build avec PyInstaller
echo.
echo [2/3] Création de l'exécutable...
pyinstaller ^
    --onefile ^
    --windowed ^
    --name "Haptic Master" ^
    --icon=icon.ico ^
    --hidden-import=pystray._win32 ^
    --hidden-import=PIL._tkinter_finder ^
    --exclude-module pkg_resources ^
    --exclude-module setuptools ^
    --exclude-module distutils ^
    --noconfirm ^
    haptic_master.py

REM Copier l'exécutable
echo.
echo [3/3] Finalisation...
if exist "dist\Haptic Master.exe" (
    echo Done
) else (
    echo Erreur lors de la création de l'exécutable
)
