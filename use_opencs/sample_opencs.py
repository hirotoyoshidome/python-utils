import cv2

# バージョンを出力
print(cv2.__version__)
# パスを指定
path = './human.jpg'
# 配列で出力
I = cv2.imread(path)
print(I)

# 新しいwindowで指定した画像を出力する
cv2.namedWindow('window')
cv2.imshow('window', I)
cv2.waitKey(0)
cv2.destroyAllWindows()
