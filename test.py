import random

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
