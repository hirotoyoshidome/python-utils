#!/bin/usr python3

import numpy as np

# 数値微分
def numerical_diff(f, x):
    h = le - 4
    return (f(x + h) - f(x - h) / (2 * h))

# 偏微分の場合は片方の関数の値を固定して上記の数値微分の関数に流すことで算出することが可能
def function2(x):
    return x[0] ** 2 + x[1] ** 2
# 上記のような変数が２つある関数に対しては偏微分を使用して算出する

# 勾配
# 微分をすることで勾配を算出する
def numerical_gradient(f, x):
    # 0で除算することのないように小さな値を設定しておく
    h = le - 4
    # 0の配列を生成する（xと同じ構造）
    grad = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)の計算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)の計算
        x[idx] = tmp_val -h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        # 値をもとに戻しておく
        x[idx] = tmp_val
        return grad

# 勾配降下法
# 勾配の値をxから引くことで徐々に勾配の値を0に近づけるようにする
# lrは学習係数である
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x

# ニューラルネットワークでは重みパラメータに対する損失関数の勾配を算出し、損失関数の値を小さくすることで最適な重みパラメータの値を学習させる


# 余談
# かんたんな関数についてはlambda記法を使用して関数を生成することも可能
f = lambda x, y: x+y
print(f(1,2)) # 3と出力

