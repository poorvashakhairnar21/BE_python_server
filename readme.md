
# create build and exe

pip install pyinstaller
pyinstaller --onefile zoroServer.py


pyinstaller --onefile --noconsole --icon=myicon.ico main.py
pyinstaller --onefile --noconsole zoroServer.py

pyinstaller zoroServer.spec
