@echo off
echo Creation de l'environnement virtuel 'venv'...
python -m venv venv

echo Activation de l'environnement...
call venv\Scripts\activate

echo Installation des dependances depuis requirements.txt...
pip install -r requirements.txt

echo.
echo L'installation est terminee. Vous pouvez maintenant lancer start_conversion.bat.
pause