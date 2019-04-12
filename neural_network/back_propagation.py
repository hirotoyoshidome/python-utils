#!/bin/usr python3

import numpy as np
import loss_function
import softmax_function

# 誤差逆伝播法
# 乗算レイヤ
class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out
    # 逆伝播ではxとyをひっくり返す
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy

# 加算レイヤ
class AddLayer:
    def __init__(self):
        pass
    def forward(self, x, y):
        out =  x + y
        return out
    # 1をかける（つまり、そのまま流す）
    def backword(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy

class Relu:
    def __init__(self):
        self.mask = None
    # 0より小さいときは0, それ以外はその値
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        return out
    # 順伝播で0なら逆伝播も0となる
    # 順伝播で0より大きいなら逆伝播ではそのまま流す
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        return dx

class Sigmoid:
    def __init__(self):
        self.out = None
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out
    # そのまま微分の計算をすると下記の通りとなる
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
        return dx

class Affine:
    # 初期化の引数で重みとバイアスをとる
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.y = None
        self.dw = None
        selef.db = None
    # 以前にやった重みのドット積にバイアスを足す
    def forward(self, x):
        self.x = x
        out = np.dot(x, slef.W) + self.b
        return out
    def backward(self, dout):
        # 重みの行列の行と列を入れ替えたもののドット積
        dx = np.dot(dout, self.W.T)
        # 重みに対しての逆伝播を求める
        self.dw = np.dot(self.x.T, dout)
        # バッチ処理に対応しているため0番目の軸に対しての総和を算出する
        self.db = np.sum(dout, asis=0)
        return dx

class SoftmaxWithLoss:
    def __init__(self):
        # 損失
        self.loss = None
        # softmaxの出力値
        self.y = None
        # 教師データ
        self.t = None
    # ソフトマックス関数と交差エントロピー誤差を利用して損失を算出する
    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss
    # 逆伝播はきれいな値(y -t)になることが知られている
    # これは損失関数の組み合わせが重要である
    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        return dx

