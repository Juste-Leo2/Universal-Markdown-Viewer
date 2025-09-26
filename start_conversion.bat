@echo off
echo Activation de l'environnement virtuel...
call venv\Scripts\activate

echo Lancement du script de conversion Python...
python main.py

echo.
echo Appuyez sur une touche pour fermer.
pause