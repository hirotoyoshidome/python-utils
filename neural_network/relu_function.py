#!/usr/bin/python3

import numpy as np
import matplotlib.pylab as plt

# ReLU関数
# 0以外はその数値をとる
# 0より小さい数値は0とする
def relu_function(x):
    return np.maximum(0, x)

# グラフを設定する
x = np.arange(-5.0, 5.0, 0.1)
y = relu_function(x)

plt.plot(x, y)
# y軸の範囲を設定する
plt.ylim(-0.9, 5.1)

plt.show()

