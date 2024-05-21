from flask import Flask
from flask_restx import Api, Resource
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
api = Api(app)

'''
<date> ex) 20240509
<kind> 종합: 'all', 시사: 'sisa', 스포츠: 'spo', 연예: 'ent', 정치: 'pol', 경제: 'eco', 사회: 'soc', 세계: 'int', IT/과학: 'its'
'''

@api.route('/<string:date>/<string:kind>')
class GetRank(Resource):
    def get(self,date,kind):
        url = 'https://news.nate.com/rank/interest?sc='+kind+'&p=day&date='+date
        req = requests.get(url)
        req.encoding = 'UTF-8'
        html = req.content.decode('UTF-8', 'ignore')
        soup = bs(html, 'html.parser', from_encoding='UTF-8')

        titles = []

        for tag in soup.find_all("h2", {"class": "tit"}):
            titles.append(tag.text)

        return titles[0]


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
