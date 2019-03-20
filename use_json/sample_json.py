import json

# ファイル読み込み
f = open("./sample.json", "r")

# jsonモジュールに流す(json -> 辞書型
jfile = json.load(f)
print(jfile['book1'])

# クラスを出力する
print('jfile:{}'.format(type(jfile)))

# 変換対象の辞書型を作成する
json_dic = {'test' : {'test_key' : 'test_val'}}

# json形式で出力(辞書型 -> json)
json_str = json.dumps(json_dic)
print(json_str)
