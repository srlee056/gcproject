

import requests
from bs4 import BeautifulSoup
import json
import os


## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gcsite.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from parsed_data.models import PlayerData,Party

def parse_guild_players():
    player_list = PlayerData.objects.order_by('-level')
    for p2 in player_list:
        #url2 = 'https://maplestory.nexon.com/Ranking/World/Total?c='
        url2 = "https://maple.gg/u/"
        req2 = requests.get(url2 + p2.name)
        print(p2.name)
        #print (url2+ p2)

        html2 = req2.text
        soup2 = BeautifulSoup(html2, 'html.parser')

        avatarImgSrc= soup2.select(
            '#user-profile > section > div > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img'
        )
        character = soup2.select(
            '#user-profile > section > div > div.col-lg-8 > div.user-summary > ul > li:nth-child(2)'
            )
        ch = character[0].text
        print(ch)
        level = soup2.select(
            '#user-profile > section > div > div.col-lg-8 > div.user-summary > ul > li:nth-child(1)'
            )
        lv = level[0].text
        #if lv.startswith('Lv.'):
        #    lv = lv[3:]
        print(lv)
        mrData = soup2.select(
            '#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(1)'
        )
        
        try:
            mrFloor = mrData[0].select(
                'section > div > div > div > h1'
            )
            mrFloor = mrFloor[0].text
        except:
            mrFloor = '0 층'
        
        mrFloor=mrFloor[:2]
        print(mrFloor)
        p2.imgSrc = avatarImgSrc[0]['src']
        p2.level = lv
        p2.character = ch
        p2.mrFloor = mrFloor
        #print(character[0].text)
        #print(mrFloor)
        if(p2.party == None):
            party = Party()
            party.id = 0
            party.name="분류 전"
            party.save()
            p2.party = party
        print(p2.party)
        p2.save()
        '''data = []

        data.append(level[0].text[3:])
        data.append(character[0].text)
        data.append(avatarImgSrc[0].src)
        player_data_dict[p2] = data

 
        player_data = soup2.select(
            '#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr.search_com_chk' 
        )
        

        for d in player_data : 
            avatarImgSrc= d.select(
                'td.left > span > img:nth-child(1)'
            )
            character = d.select('td.left > dl > dd')
            level = d.select('td:nth-child(3)')
            print(avatarImgSrc[0].src)
            print(p2+ level[0].text)

            print(character[0].text)
            data = []

            if level==None:
                level[0].text = ""
            data.append(level[0].text[3:])
            data.append(character[0].text)
            data.append(avatarImgSrc[0].src)
            player_data_dict[p2] = data'''
           
    player_data_dict ={}
    return player_data_dict    

if __name__ =='__main__':
    player_data_dict = parse_guild_players()
    
    '''for p, d in player_data_dict.items():
        playerdata = PlayerData
        PlayerData(imgSrc = d[2], name = p, character = d[1],level = d[0], mrFloor=).save()
        print("start crwaling")
    player_data_dict = parse_guild_players()
    print("done crwaling")
    for p, d in player_data_dict.items():
        playerdata = PlayerData.objects.create(
        imgSrc=d[2],
        name=p,
        character=d[1],
        level = d[0]
    )
        
        '''
