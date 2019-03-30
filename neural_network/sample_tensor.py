#!/usr/bin/python3

import numpy as np

# 多次元配列の基本を実装する

# 一次元配列
A = np.array([1, 2, 3, 4])
print(A)

# 次元を出力する
print(np.ndim(A))

# 構造を出力する
# タプルで出力する
print(A.shape)
# タプルのためインデックスで参照することができる
print(A.shape[0])

# 二次元配列
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B))
print(B.shape)


# 行列の積
# 要素数が一致していないと例外が発生する
# ドット積を算出する
C = np.array([[1, 2], [3, 4], [5, 6]])
D = np.array([7, 8])
# ドット積を算出
# 内部的には1*7+2*8, 3*7+4*8, 5*7+6*8を計算している
print(np.dot(C, D))

# ニューラルネットワークではドット積を利用して計算している
# 入力値または中間値と重みをドット積で計算している

