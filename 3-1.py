from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

f = open('Exam3_1.txt','w')

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options = options)
driver.get("https://gogakuru.com/english/phrase/genre/180_%E5%88%9D%E7%B4%9A%E3%83%AC%E3%83%99%E3%83%AB.html?pageID=1&layoutPhrase=1&orderPhrase=1&condMovie=0&perPage=50&flow=enSearchGenre&condGenre=180")

result = driver.find_elements(By.CLASS_NAME,"font-en")

print(len(result))

for x in result:
    # print(x.text)
    f.write(x.text+"\n")

f.close()
driver.close()