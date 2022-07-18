# Python
專題一　Technews　https://drive.google.com/file/d/1R03f5_QFZWWp6k84vB8psK9IsH1n1HQf/view

1-1 
爬取網址: https://technews.tw/

1-2 
開啟 Exam1_1 檔案,使用檔案裡面提供的連結,去爬報導內的正文內容文字
一個 url 則產生一個 txt 檔,內容為 url 的正文文字
sum_title_url 連結所爬的 txt 檔名為 sum_對應的 category_ sum_title 的前 4 個字
spotlist 連結所爬的 txt 檔名為 spot_對應的 category_ title 的前 4 個字


專題二　News API　https://drive.google.com/file/d/1qly8Fzuzl-ovJ0Z7mwehSLxQ6USOIF9i/view

2-1 
研讀 NewsAPI: https://newsapi.org/  
使用 python(請使用: from newsapi import NewsApiClient 的語法取資料,不要用requests.get),  
控制 newsapi 裡面的選項取得報導,且報導須滿足以下要求:
*標題或報導內容一定要有 "武漢肺炎" 或 "新冠肺炎" 四個字,且一定不能出現 外遇 兩個字
*爬出來的新聞只能來自 ETtoday , 風傳媒, 中國時報, 聯合新聞網
*由新到就排序
*一頁呈現 100 篇報導

2-2 
加分題 : 再使用requests.get語法讀取資料


專題三　同時儲存檔案及存入資料庫　https://drive.google.com/file/d/1aIw9lUrz-ExrCn1L7Z-kVcqSRjjGtF3S/view  
爬取網址: https://gogakuru.com/english/phrase/genre/180_%E5%88%9D%E7%B4%9A%E3%83%AC%E3%83%99%E3%83%AB.html?layoutPhrase=1&orderPhrase=1&condMovie=0&flow=enSearchGenre&condGenre=180&perPage=50  
請把網頁的所有英文句子(EX. You bet!)(只要文字)用 SLENIUM 抓下來,且爬取的時候不顯示螢幕,並把爬下來的語料存成三種形式:  
3-1 txt  
3-2 直接串資料庫存入  
3-3 pickle (課程中沒有此部分,請自我突破)
