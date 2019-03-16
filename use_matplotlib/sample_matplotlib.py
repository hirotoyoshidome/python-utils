import matplotlib.pyplot as plt
import numpy as np

# 変数Xに数列の始点が-π(-3.14..)、終点がπ(3.14..)、 要素数50、endpoint(生成する数列に終点を含むか否か)
X = np.linspace(-np.pi, np.pi, 50, endpoint=True)
print(X)

# サイン(sin)、コサイン(cos)の値をとる
C, S = np.cos(X), np.sin(X)
print(C)
print(S)
# コサイン(cos)のグラフを描画する
plt.plot(X, C)
# サイン(sin)のグラフを描画する
plt.plot(X, S)

# 第一引数(配列(リスト))がx軸、第二引数(配列(リスト))がy軸⇒数列のこと
# plt.plot([1, 2], [8, 16])

# 別ウィンドウでグラフを出力する
plt.show()
