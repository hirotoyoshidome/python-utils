#!/bin/usr python3

# 確率的勾配降下法(stochastic gradient descent)
class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]

