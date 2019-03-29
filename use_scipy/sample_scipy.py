from scipy import integrate, linalg
import numpy as np

# 積分
# 2x + 5のこと
def func(x):
    return 2*x + 5

# 2x + 5を積分すると
# 2 * 1/2 * x^2 + 5 * x + c
# すなわち
# x^2 + x^2 + c
# 5を代入すると
# 積分結果は50
# 誤差(cのこと)

res, err = integrate.quad(func, 0, 5)

print("積分結果：{0}, 誤差：{1}".format(res, err))

# 行列
# numpy
narray = np.array([[1, 2], [3, 4]])

# numpyでリストより生成した配列(行列)の逆行列を取得する
inv_narray = linalg.inv(narray)
print("narrayの逆行列：{}".format(inv_narray))

# 逆行列より行列式を取得する
res_det = linalg.det(inv_narray)
print("inv_narrayの行列式：{}".format(res_det))

# 逆行列よりノルムを取得する
inv_narray_norm = linalg.norm(inv_narray)
print("inv_narrayのノルム：{}".format(inv_narray_norm))

