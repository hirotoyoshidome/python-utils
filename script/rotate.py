#!/bin/usr/python3

# 空港で暇だからなんかしらスクリプトを作成してみる
# work配下の構造を取得して最終更新日を取得＆処理をかけてみる

import os
import datetime as dt

# ディレクトリを設定
tar_dir = './work/'

# 拡張子を設定
file_type = '.txt'

# 設定したディレクトリの構造を取得する
tar_list = os.listdir(tar_dir)

for li in tar_list:
    if file_type in li:
        print(li + "はテキストファイルです")
        # テキストファイルであれば、最終更新日を取得する
        # タイムスタンプの出力形式をフォーマットしつつ最終更新日を取得する
        print(dt.datetime.fromtimestamp(os.stat(tar_dir+li).st_mtime))
        # ここに削除なり、ローテートなりを書けば使用できそう

    else:
        print(li + "は対象外です")
