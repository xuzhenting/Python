import requests
from bs4 import BeautifulSoup
import json

# api_key='5fbdd2020d99423a9a8c7d9786951d95'
# q = '+新冠肺炎, -外遇'
# domains = 'ettoday.net , storm.mg , chinatimes.com , udn.com'
# language = 'zh'
# sort_by = 'relevancy'
a="q=+新冠肺炎, -外遇&domains=ettoday.net,storm.mg,chinatimes.com,udn.com&language=zh&sort_by=relevancy&apiKey=5fbdd2020d99423a9a8c7d9786951d95"
response = requests.get("https://newsapi.org/v2/everything?"+a)
soup = BeautifulSoup(response.text, "html.parser")
f = open('Exam2_2.json','w',encoding='UTF-8')
b = soup.text
print(soup)
f.write(b)
f.close()