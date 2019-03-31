#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 文字コードの指定をしないと動かなかったので追加(ubuntuにしたからかも)

# 手書き数字認識
# オライリーのMNISTのデータを使用して実装する

import sys, os
# 親のディレクトリのファイルをインポートするための設定
sys.path.append(os.pardir)
import numpy as np
import pickle
from dataset.mnist import load_mnist
from PIL import Image

# シグモイド関数
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

# ソフトマックス関数
def softmax_function(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / sum_exp_x
    return y

# PILモジュールを使用して画像を出力する
def img_show(img):
    # 配列からデータオブジェクトへの変換はfromarrayメソッドで行っている
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# データを取得する
# normalizeは値を0-1の間の値に正規化、flattenは一次元配列に変換、one_hot_labelは正解のラベルが1,それ以外が0となるように格納する設定を有効化
def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

# サンプルで重みの設定がされたpickleファイルを読み込んでネットワークの初期化をする
# pickleはpythonで扱えるデータのことで初回にダウンロードすることで次回のアクセスのときにキャッシュみたいな感じでそこから取得できるようにするデータみたい
def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network

# ニューラルネットワークの処理
def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid_function(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid_function(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax_function(a3)
    return y

# main実行
x, t = get_data()
network = init_network()

# 正解した件数を取得する
accuracy_cnt = 0

# 入力値の件数回す
for i in range(len(x)):
    y = predict(network, x[i])
    # 一番確率の大きいものを取得
    p = np.argmax(y)
    # ラベルで設定されている値（正解の値）と比較して一致している場合はカウントする
    if p == t[i]:
        accuracy_cnt += 1

# 確率を取得する
print("Accuracy : " + str(float(accuracy_cnt) / len(x)))

# 画像出力
img = x[0]
label = t[0]
print(label)

# flatten=Trueを設定しているため784の一時配列となっている
print(img.shape)
# 画像を出力するためリシェイプする
img = img.reshape(28, 28)
# 28, 28の二次元配列になっていることを確認する
print(img.shape)

img_show(img)

