#!/usr/bin/python3

import numpy as np

# 3層ニューラルネットワークを構築する

# ニューラルネットワークでは非線形の曲線のシグモイド関数を活性化関数として利用する
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

# 恒等関数は入力値をそのまま出力する関数のこと
def identity_function(x):
    return x

# 重みとバイアスを設定する(実際はここを学習させる)
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network

# 順方向の伝播
# 入力値または中間値と重みを乗算し、バイアスを加算する
# 上記の結果を活性化関数(ここではシグモイド関数)にながす
# 出力層(最後)は恒等関数にながして結果を得る
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid_function(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid_function(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y

network = init_network()
# ここで入力値を設定する
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)

