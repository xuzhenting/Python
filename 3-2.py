from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017) 
db = client["testDatabase"]
collection = db["testTable"]

f = open('Exam3_1.txt','w')

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options = options)
for page in range(1,4):
    driver.get("https://gogakuru.com/english/phrase/genre/180_%E5%88%9D%E7%B4%9A%E3%83%AC%E3%83%99%E3%83%AB.html?pageID="+str(page)+'1&layoutPhrase=1&orderPhrase=1&condMovie=0&perPage=50&flow=enSearchGenre&condGenre=180')
    result = driver.find_elements(By.CLASS_NAME,"font-en")
    print(len(result))

    mongo = []
    for i , x in enumerate(result):
        # print(x.text)
        f.write(x.text+"\n")
        d = {}
        i += 1
        d["item"] = i
        d["message"] = x.text
        mongo.append(d)

    print(mongo)
    collection.insert_many(mongo)

f.close()
driver.close()