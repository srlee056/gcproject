

import requests
from bs4 import BeautifulSoup
import json
import os



## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

player_list = []
for i in range(1, 11) :
    url = 'https://maplestory.nexon.com/Common/Guild?gid=830734&wid=3&orderby=0&page='
    req = requests.get(url + str(i))
    #print (url+ str(i))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    player = soup.select(
        '#container > div > div > table > tbody > tr'
    )
     
    for p in player :
        player = p.select('td.left > dl > dt > a')[0].text
      #  print(player)
        player_list.append(player)
        
    #    print(p.select('td.left > dl > dd')[0].text)
    #    print(p.select('td:nth-child(3)')[0].text)

#print(player_list)

for p in player_list:
    url2 = 'https://maplestory.nexon.com/Ranking/World/Total?c='
    req2 = requests.get(url2 + p)
    print (url2+ p)

    html2 = req2.text
    soup2 = BeautifulSoup(html2, 'html.parser')

    player_data = soup2.select(
        '#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr.search_com_chk' 
    )

    for d in player_data : 
        avatarImgSrc= d.select(
            'td.left > span > img:nth-child(1)'
        )
        character = d.select('td.left > dl > dd')
        level = d.select('td:nth-child(3)')

        print(p+level[0].text)
    #print(character[0].text)
    

data = {}

data['imgSrc'] = avatarImgSrc
data['name'] = name[0].text
data['char'] = character[0].text
data['level'] = level[0].text
