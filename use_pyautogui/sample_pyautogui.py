import pyautogui

# スクリーンのサイズを取得する
screen_x, screen_y = pyautogui.size()

print(screen_x)
print(screen_y)

# カーソルを動かしてみる
pyautogui.moveTo(screen_x-200, screen_y-200, duration=1)

# 右クリックしてみる(メニューの表示)
pyautogui.rightClick()

# 同時入力を実行するときはhotkeyメソッドが便利
pyautogui.hotkey('win', 'd')

# デスクトップ画面のスクリーンショットを取得してみる(コミットしてません)
pyautogui.screenshot('./screenshot.png')

# もどる
pyautogui.hotkey('win', 'd')

# 他にもPCで操作できることは自動化できるみたいだけどモジュールがないため、冪等性は担保されない
# フォーム入力とかも自動化できるみたい(タブキーで入力フォームを変更することで)
# GUIオートメーションという
