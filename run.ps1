& .\venv\Scripts\Activate.ps1
$env:APP_SETTINGS="config.ProductionConfig"
#python .\app.py
.\venv\Scripts\waitress-serve.exe --call 'app:create_app'
