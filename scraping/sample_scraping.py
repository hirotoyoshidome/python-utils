import requests
import bs4

url = 'https://www.yahoo.co.jp/'

# GETでYahooのトップ画面にアクセスする
res = requests.get(url)
# ステータスコードが200以外で例外を発生させる
res.raise_for_status()
# ステータスコートが返る(Responseオブジェクト)
print(res)

# HTMLを解析する(contentまたはtextでもいけるみたい)
html = bs4.BeautifulSoup(res.content, 'html.parser')
# print(html)

# 抽出する
reslist = html.select("a")

for tag in reslist:
    print(tag.getText())

