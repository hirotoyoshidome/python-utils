#!/usr/bin/python3

import numpy as np

# ソフトマックス関数
def softmax_function(x):
    # 自然対数を利用するため容易に扱えない桁数になってしまいオーバーフローをおこす
    # 対策として事前に一番大きいものを減算しておくことで対応する
    c = np.max(x)
    # 自然対数をとる
    exp_x = np.exp(x - c)
    # 引数で渡された値のΣ(合計)の値をとる(こちらも-cが適用されている)
    sum_exp_x = np.sum(exp_x)
    # 分子に入力信号の指数関数、分母にすべての入力関数の指数関数の和をとる
    y = exp_x / sum_exp_x
    # 分子分母に-c の値が適用されているため結果には影響はない
    return y

# 入力値を設定
x = np.array([0.3, 2.9, 4.0])
y = softmax_function(x)
print(y)

# ソフトマックス関数では0-1の値の数値を結果として返却するが返却された値の和は1となる
# そのため確率として利用することができる
print(np.sum(y))

