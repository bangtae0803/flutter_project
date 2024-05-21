import requests
from bs4 import BeautifulSoup as bs

date = '20240509'
kind = 'all'
# 기사 사이트 링크
url = 'https://news.nate.com/rank/interest?sc='+kind+'&p=day&date='+date
req = requests.get(url)
soup = bs(req.text, 'html.parser')
titles = []
for tag in soup.find_all("h2", {"class": "tit"}):
    titles.append(tag.text)

print(titles[0])