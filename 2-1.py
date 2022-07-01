from newsapi import NewsApiClient
import json
f = open('Exam2_1.json','w',encoding='UTF-8')
# Init
newsapi = NewsApiClient(api_key='5fbdd2020d99423a9a8c7d9786951d95')

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',sources='bbc-news,the-verge',category='business',language='en',country='us')

# /v2/everything
all_articles = newsapi.get_everything(q = '+新冠肺炎, -外遇',
                                      domains = 'ettoday.net , storm.mg , chinatimes.com , udn.com',
                                      language = 'zh',
                                      sort_by = 'relevancy')

# /v2/top-headlines/sources
# sources = newsapi.get_sources()

json.dump(all_articles,f,ensure_ascii=False)
f.close()