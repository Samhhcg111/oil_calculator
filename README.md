這是精油調配器的起點
# windows
# 環境安裝
py -m venv pyenv
pip install -U pip
pip install -r requirements.txt
# 打包
pyinstaller ./oil_app.spec

# 畫面
![gui_demo](./gui_demo.jpg)