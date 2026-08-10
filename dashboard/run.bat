@echo off
cd /d "%~dp0"
if not exist .venv (
  echo Criando venv...
  python -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install -q -r requirements.txt
echo.
echo Abra no desktop:  http://localhost:8799
echo No celular (mesma Wi-Fi): http://SEU-IP-LOCAL:8799   (veja com ipconfig)
echo.
python app.py
pause
