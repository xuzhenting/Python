import requests
from bs4 import BeautifulSoup
import json

f = open('Exam1_1.json','r')
content = f.read()
f.close()
j = json.loads(content)
# print(j[0]["sum_title_url"])

for x in range(len(j)):
    response = requests.get(j[x]["sum_title_url"])
    soup = BeautifulSoup(response.text, "html.parser")
    sumname = "sum_"+j[x]["category"]+"_"+j[x]["sum_title"][:4]+'.txt'
    print(sumname)
    f = open(sumname,'w',encoding='UTF-8')
    a = soup.find("div", {"class":"indent"}).findAll("p")
    for b in a:
        print(b.text)
        f.write(b.text)


    for y in range(len(j[x]["spotlist"])):
        response = requests.get(j[x]["spotlist"][y]["url"])
        soup = BeautifulSoup(response.text, "html.parser")
        spotname = "spot_"+j[x]["category"]+"_"+j[x]["spotlist"][y]["title"][:4]+'.txt'
        print(spotname)
        f = open(spotname,'w',encoding='UTF-8')
        a = soup.find("div", {"class":"indent"}).findAll("p")
        for b in a:
            print(b.text)
            f.write(b.text)