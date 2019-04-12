#!/bin/usr python3

import numpy as np

# 2乗和誤差
def mean__squared_error(y, t):
    return 0.5 * np.sun((y-t) ** 2)

# 交差エントロピー誤差
def cross_entropy_error(y, t):
    delta = le - 7
    return -np.sum(t * np.log(y + delta))
