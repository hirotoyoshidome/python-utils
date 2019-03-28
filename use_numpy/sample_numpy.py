import numpy as np

# numpyはnpとエイリアスをつけるのが慣習みたい

# 二次元配列(行列)
ary = np.array([[1,2], [3,4],[5,6]])
print(ary)

# numpyはc言語で最適化されているためpythonのリストよりも配列に変換して計算を行った方が実行速度が速い
# ちなみにpythonのfor文は遅くて有名

ar1 = np.array([1.0, 2.0, 3.0])
ar2 = np.array([4.0, 5.0, 6.0])

# 各要素ごとに計算をする
print(ar1 + ar2)

# マイナスの計算もできる
print(ar1 - ar2)

# 乗算、除算もできる
print(ar1 * ar2)
print(ar1 / ar2)
# これらの計算は要素の数があっていないとエラーになる

# ブロードキャストといってスカラ値と計算することもできる
print(ar1 * 3)

# 要素へのアクセスはインデックスを利用してできる
print(ar1[1])

# 一時配列に変換することもできる
ar3 = np.array([[1.0, 2.0], [3.0, 4.0]])
ar3_flat = ar3.flatten()
# 4.0が出力されるはず
print(ar3_flat[3])

# こんな出力もできる
# True or Falseで出力
print(ar3_flat > 1)

# 当てはまるものを出力
print(ar3_flat[ar3_flat > 1])

