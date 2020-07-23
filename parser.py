#https://maplestory.nexon.com/Ranking/World/Total?c=%EC%9E%89%EC%84%9C%EB%A6%BC

import requests
from bs4 import BeautifulSoup
import json
import os

## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://maplestory.nexon.com/Ranking/World/Total?c=기후쨘쨘')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
#print (html)

tags = soup.findAll('tr', attrs={'class': 'search_com_chk'})

print (tags)
data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)