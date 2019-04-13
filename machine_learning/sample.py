#!/bin/usr python3

# クラス分類(classifcation)

# 有名なアイリスの花の分類問題
# データセットはscikit-learnのライブラリの中に含まれている

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display
from sklearn.neighbors import KNeighborsClassifier

# データをロードする
iris_dataset = load_iris()

# データを確認してみる
print("{}".format(iris_dataset.keys()))
print("{}".format(iris_dataset['target_names']))
print("{}".format(iris_dataset['feature_names']))
print("{}".format(iris_dataset['data'][:5]))

# 訓練データとテストデータを分ける
#  慣習的に2次元配列（行列）をXで、1次元配列（ベクトル）をyで表現する
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
# 通常、訓練データ：テストデータ=3:1でわけられるみたい（決まりはない）

# データを検査するため散布図を作成する
# X_trainのデータからPandasのDataFrameを作成する
# カラムに名前をつける
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)

# データフレームからscatter matrixを作成し、y_trainに従って色をつける
# データとしてデータフレームとy_trainをとり、図のサイズ、マーカー、色付けを設定する
grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
# 出力
plt.show()

# k-最近傍法(k-Nearest Neighbors)
# これは訓練セットを渡すだけで新しいでターポイントに対して予測する際に新しい点に最も近い点を訓練セットから探し出し、新しい点に近かった点のラベルを新しいデータポイントに与える
# kは新しい点に最も近い1点だけを用いるのではなく、訓練セット中の固定されたk個の近傍点を用いることができる点を意味する
# ここでは近傍点は1で実装する

# インスタンスを生成する
knn = KNeighborsClassifier(n_neighbors=1)

# 訓練データを渡す(モデルの構築)(fitメソッドの返り値はKNeighborsClassifierオブジェクトであり、パラメータ(設定しないとデフォルト値)を確認することができる)
knn.fit(X_train, y_train)

# 予測を行う
X_new = np.array([[5, 2.9, 1, 0.2]])
# 上記の場合、ガクの長さが5cm、ガクの幅が2.9cm、花弁の長さが1cm、花弁の幅が0.2cmである花を分類するように設定している
# scikit-learnでは入力データは2次元配列であることが前提のためデータ形式を合わせる

# 予測の実施
prediction = knn.predict(X_new)
# 配列のインデックスで出力されるため名前を確認し出力する
print("{}".format(iris_dataset['target_names'][prediction]))

# モデルの評価
# 訓練で使用していないテストセットを使用してモデルの評価を実施する
# 精度(accuracy)を算出して測定をする

# テストデータの予測を実施する（結果は配列のインデックスで出力）
y_pred = knn.predict(X_test)

# 結果の確率を出力する(0-1の値で小数点以下2桁の小数で出力)
print("{:.2f}".format(np.mean(y_pred == y_test)))
# 下記でも出力できる
print("{:.2f}".format(knn.score(X_test, y_test)))
# 上記の結果は0.97が出力されるため97%の確率で分類が成功していることを表す

# 上記の例ではk-最近傍法を使用して予測を実施した
# scikit-learnではfit, predict, scoreは共通するインターフェースである

