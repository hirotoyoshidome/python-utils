import csv

# ファイルを読み込む
f = open("./sample.csv", "r")

# csvモジュールに渡す
reader = csv.reader(f)
# ヘッダを取得する
header = next(reader)

print(header)

# ループして取得する
for row in reader:
    print(row)

# きちんと閉じる
f.close()
