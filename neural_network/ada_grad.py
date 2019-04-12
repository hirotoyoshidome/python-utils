#!/bin/usr python3

# AdaGrad
# 過去の勾配を2乗和として記録する(下記のソースでは変数hが相当するもの)
# 学習を進めれば、更新の度合いは小さくなる

import numpy as np

class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + le-7)

# sqrtはルート（√）を計算している
# le-7は0で除算をしないように小さな値を足している

