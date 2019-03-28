#!/usr/bin/python3

import numpy as np
# ADNゲート
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

# NANDゲート(重みとバイアスだけが異なる(Not ANDでは符号が反転する))
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

# ORゲート(重みとバイアスだけが異なる)
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

# XORゲートは非線形のためニューロンを多層化して表現する
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)

# main
print("単純パーセプトロン")
print("ANDゲート")
print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))

print("NANDゲート")
print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))

print("ORゲート")
print(OR(0,0))
print(OR(1,0))
print(OR(0,1))
print(OR(1,1))

print("多層パーセプトロン")
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))

