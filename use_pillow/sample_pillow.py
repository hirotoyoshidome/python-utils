from PIL import Image
import numpy as np

path = './human.jpg'

# 画像を取得する
img = Image.open(path)

# 画像サイズを取得する
width, height = img.size

print(width)
print(height)

# 画像ファイルを配列化する
img_pixel = []

# 左上がx, y = 0, 0となるためその順で詰めていく(矩形(くけい))右に行くほど、下に行くほどxとyの値は増加する
for y in range(height):
    for x in range(width):
        img_pixel.append(img.getpixel((x, y)))

# numpyで配列に変換しておく
img_pixels = np.array(img_pixel)

# RGBで配列に格納されているため出力してみる
print(img_pixels[0])

# 配列に変換しない場合はタプルで出力される(ちなみに[0]をつけないとすべてが出力される)
print(img_pixel[0])

# 画像を出力する(saveなら保存できる)
img.show()

# そのた画像の修正や、図形の描写とかもできるみたい(省略)
