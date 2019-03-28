# クラス
class Main:
    # コンストラクタ(Main()でインスタンスが作成されたときに呼び出される)
    def __init__(self):
        print("コンストラクタです")
        print("初期化処理をします")

    # pythonでは引数の最初にself(自分自身)をとるのが一般的らしい
    def greet(self):
        print("Hello")

# インスタンスの作成はこれで行ける
insta = Main()
# メソッドを利用する
insta.greet()

