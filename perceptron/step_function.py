#!/usr/bin/python3

import numpy as np
import matplotlib.pylab as plt

# ステップ関数
# 0より大きい時は発火する
def step_function(x):
    return np.array(x > 0, dtype=np.int)

# xの範囲とステップ数を指定する
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)

plt.plot(x, y)

# y軸の範囲を指定する
plt.ylim(-0.1, 1.1)
plt.show()
