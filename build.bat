virtualenv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
pyinstaller --onefile .\src\barcode-generator.py
