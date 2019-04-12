#!/bin/usr python3

import util
import numpy as np

# CNN(Convolutional Neural Network)の部品となる畳み込み層とプーリング層の実装
class Convolution:
    # 重み、バイアス、ストライド、パディングを引数にもつ
    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad
    def forward(self, x):
        # 重み（ここではフィルター）の数、チャンネル、高さ、幅を設定する
        FN, C, FH, FW = self.W.shape
        # 入力データの値も設定する
        N, C, H, W = x.shape
        # 出力するときの高さと幅を設定する
        out_h = int(1 + (H + 2 * self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2 * self.pad -FW) / self.stride)

        # im2colメソッドを使用して行列に展開する
        col = im2col(x, FH, FW, self.stride, self.pad)
        # -1を指定することで環境に合うように自動で値を設定してくれる。Tは行と列を入れ替える
        # 処理内容は計算しやすいように上記の処理で行列に変換しているため、重みも整形している
        col_W = self.W.reshape(FN, -1).T
        out = np.dot(col, col_W) + self.b
        # 出力データも整形して出力する(transposeは設定したインデックスの順に整形する)
        out = out.rehape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)
        return out



