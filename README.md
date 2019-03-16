# python-tools
## Pythonで作成したツールを格納する。
* ファイル読み込み
* OpenCVサンプル


## pip
* pipを最新バージョンにする

```
python -m pip --upgrade pip
```

* opencvをインストールする

```
pip install opencv-python
```

* Pyinstallerをインストールする

```
pip install pyinstaller
```

exeファイル作成

```
pyinstaller xxx.py -onefile
```
でexeファイルを作成することができる(C言語のはずのためpython環境がなくても実行できる)
⇒かなり多くのファイルが作成されるため注意

