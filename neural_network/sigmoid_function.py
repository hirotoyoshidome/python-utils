#!/usr/bin/python3

import numpy as np
import matplotlib.pylab as plt

# シグモイド関数
# 自然対数を利用する
# 非線形の曲線のグラフになる
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

# シグモイド関数にながす
sa = np.array([-1.0, 1.0, 2.0])
print(sigmoid_function(sa))

# グラフを設定する
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid_function(x)

plt.plot(x, y)
# y軸の範囲を設定する
plt.ylim(-0.1, 1.1)

plt.show()

