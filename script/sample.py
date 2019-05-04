import random
import pprint
import re
import os
import shutil
import traceback
import logging
import time
import datetime
import pyperclip
import threading
import subprocess

print('hello world')

str = 'a'

print("数字を入力してください")
# ユーザーに入力させるのは文字列で返却されるためキャスト整数型に変更する必要がある
inte = int(input())

# pythonでインデントが4つらしい
if inte == 2:
    print('2です')
elif inte == 3:
    print("３desu")
else:
    print('その他です')

# pythonでは真偽値はTrue, Falseの様に先頭は大文字で記述すること
integ = 0
while True:
    print(integ)
    integ = integ + 1
    if integ == 5:
        break
print("for文")
# for文も使用できる
for i in range(3, 5):
    print(i)

# randomのモジュールを使用してみる(モジュールのインポート)
print("ランダムな数字を出力します")
print(random.randint(1,10))

# 文字列、タプルはイミュータブル(不可変)、リストはミュータブル(可変)である
# リストはいわゆる配列のことであり、タプルはイミュータブルな配列のことである
# 変更がないものはタプルを使用した方がpythonっぽいかも(実行速度も若干早くなるっぽい)

# 文字列
moji = "moji"

# リスト
ary = ["li", "arr"]

# タプル
sample_tuple = ("li", "tup")

# 参照の仕方は他と一緒

# 関数
def greeting(name):
    print("こんにちは" + name + "さん")

# return は必須
def sum(in1, in2):
    return in1 + in2

# 関数を利用する
greeting("yoru")
print(sum(5, 8))

# javaはnull, Rubyはnil, python はNoneを使用するみたい
print(None)

# 辞書型は参照渡しのものである(いわゆるMapのこと、RubyではHashというがPythonでは辞書というらしい)
# setdefaultメソッドを使用するとデータがない時に初期値を設定してくれる様になる
map = {"key": "value", 1:1}
print(map.get("key", ""))

# pprintモジュールを使用すると整形して出力してくれる(Rubyのppモジュールみたいな感じ)
pprint.pprint(map)

# 正規表現
tar = "I'm not teenager, I'm 21"
regexp = re.compile(r'[0-9]{1,3}')
res = regexp.search(tar)
print(res.group())

# 正規表現の記法はもちろん一緒
# subメソッドで置換することもできる
# compileメソッドの引数にreモジュールの定数を渡すことで正規表現検索に柔軟性を持たせることができる

# osモジュールを使用する
# カレントディレクトリを出力する
print(os.getcwd())

# 階層を渡り歩いて出力する
for name, subs, names in os.walk('../'):
    print(name)
    for sub in subs:
        print(sub)
    for of_name in names:
        print(of_name)

# shutilモジュールを使用する(shell util)
# カレントディレクトリのディスク使用量を出力する
print(shutil.disk_usage('./'))

# ファイル読み込み
path = './read_file/sample.txt'
print(open(path).read())

# ファイル書き込み(上書き)
open(path, "w").write('override')
print(open(path).read())

# 追記
open(path, "a").write('add')
print(open(path).read())
# バイナリデータのときはwbを指定する

# 例外ハンドリング
# tracebackモジュールを使用することでトレースを出力することができる
try:
    raise ValueError("error")
except ValueError as e:
    print(e)
    traceback.print_exc()

# ログのファイル出力
logging.basicConfig(filename = "sample.log", level = logging.DEBUG)
logger = logging.getLogger()
logger.debug("debug log")

# 時間を出力する(1970年からの経過秒)
print(time.time())
# 現在の日付を出力する
now = datetime.datetime.now()
print(now)

# pyperclipを使ってみる
# コピーしているテキストを出力する
copy_text = pyperclip.paste()
print(copy_text)

# クリップボードにコピーする
text = "sample"
pyperclip.copy(text)
print("クリップボードにコピーしました")

# 並列処理を実行する

def func1():
    while True:
        print("func1")
        time.sleep(1)

def func2():
    while True:
        print("func2")
        time.sleep(1)

# スレッドを設定する
thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

# スレッドをスタートする
# 別のスレッドで実行されているため順不同で出力される
thread1.start()
thread2.start()

# サブプロセス(外部コマンド)を実行する
# windowsで実行するときはshellオプションをつける必要があるみたい
subprocess.run("dir", shell=True)
