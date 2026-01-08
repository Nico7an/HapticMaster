@echo off
echo ========================================
echo Test Haptic Master for Windows
echo ========================================
echo.
echo Installation des dependances...
pip install -q -r requirements.txt

echo.
echo Lancement de l'application...
echo.
echo IMPORTANT: Configurez d'abord Logi Options+ avec le raccourci:
echo   Alt + F12  --^>  Haptic Feedback
echo.
python haptic_master.py
