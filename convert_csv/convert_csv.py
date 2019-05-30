#!/bin/usr python3

# Scrape HackerNews -> Convert CSV file

import csv
import requests
from bs4 import BeautifulSoup
import csv

target_url = "https://news.ycombinator.com/"

response = requests.get(target_url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# HTMLを出力
# print(soup.prettify())

tags = soup.find_all('a', class_="storylink")
# 出力用にリストを生成する
output_list = []

# CSV出力する値をリストに格納する
for tag in tags:
    tmp_list = []
    # タイトルを出力
    # print(tag.string)
    tmp_list.append(tag.string)
    # URLを出力
    # print(tag.get('href'))
    tmp_list.append(tag.get('href'))
    output_list.append(tmp_list)

file = open('./hacker_news_top.csv', "w")
writer = csv.writer(file, lineterminator='\n')

for li in output_list:
    writer.writerow(li)

file.close()