import requests
from bs4 import BeautifulSoup
f = open('Exam1_1.json','w')
response = requests.get("https://technews.tw/")
soup = BeautifulSoup(response.text, "html.parser")
import json

div = soup.find_all("li", class_ = "block2014")
e=[]
for x in div:
    a = {}
    cat01 = x.find("div", class_ = "cat01")
    H3 = x.find("h3")
    url = x.find("a")
    a["category"]=cat01.text
    a["sum_title"]=H3.text
    a["sum_title_url"]=url["href"]
    d=[]
    spotlict = x.findAll("li",class_="spotlist")
    for y in spotlict:
        c = y.find("a")
        b = {}
        b["title"]=c.text
        b["url"]=c["href"]
        d.append(b)
    a["spotlist"]=d
    e.append(a)
json.dump(e,f)
f.close()