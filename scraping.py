import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import time
import datetime as dt
import json
import csv

base_url = "https://economictimes.indiatimes.com/archivelist/"
base=39083

base_date = dt.datetime(2007,1,1)
start_date = dt.datetime(2019,1,1)
end_date = dt.datetime(2020,1,1)
delt = dt.timedelta(days=1)

f=open('headlines19.json','w',encoding='utf-8')
all_data={}
final_news = []
for i in np.arange(start_date,end_date,delt).astype(dt.datetime):
    num_days = (i-base_date).days
    starttime = str(base+num_days)
    year = str(i.year)
    month = str(i.month)
    
    url = base_url + "year-"+year+",month-"+month+",starttime-"+starttime+".cms" 

    r = requests.get(url)
    coverpage = r.content

    soup = BeautifulSoup(coverpage, 'html.parser')
    news_cols = soup.find_all('td', class_='contentbox5')

    data = {}
    data['Date']= i.strftime("%Y-%m-%d")
    headlines=''
    for news_col in news_cols:
        news_all = news_col.find_all('li')
        count = 0
        for news in news_all:
            headline = news.find('a').get_text()
            if headline:
                headlines += headline + '.'
    data['headlines']=headlines
    if i.day == 1:
        print(month,year)
        #print(data)
    final_news.append(data)

all_data['news']=final_news           

json.dump(all_data,f,ensure_ascii=False)
f.close()