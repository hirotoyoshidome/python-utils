import selenium.webdriver as webdriver
# import chromedriver_binary
import time

# URLを設定する
url = "https://www.yahoo.co.jp/"
# ドライバーのパスを設定する(importでうまくいかなかったためchrome73バージョンのexeファイルをダウンロードして同ディレクトリに配置)
path = "./chromedriver.exe"

# ドライバーインスタンスを取得する
driver = webdriver.Chrome(path)
# GETで通信する(ブラウザで開く)
driver.get(url)
# サーチボックスのオブジェクトを取得する
search_box = driver.find_element_by_id('srchtxt')
# サーチボックスに入力する
search_box.send_keys('退屈なことはPythonにやらせよう')
# 送信する
search_box.submit()
# 5秒待つ
time.sleep(5)
# ブラウザを閉じる
driver.quit()
