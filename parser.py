

import requests
from bs4 import BeautifulSoup
import json
import os


## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gcsite.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from parsed_data.models import PlayerData

def parse_guild_players():
    player_list = []
    for i in range(1, 11) :
        url = 'https://maplestory.nexon.com/Common/Guild?gid=830734&wid=3&orderby=0&page='
        #print (url+ str(i))
        headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'}
        req = requests.get(url + str(i), headers=headers)

        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        players = soup.select(
            '#container > div > div > table > tbody > tr'
        )
        
        for p in players :
            player = p.select('td.left > dl > dt > a')[0].text
            #print(player)
            player_list.append(player)
            
        #    print(p.select('td.left > dl > dd')[0].text)
        #    print(p.select('td:nth-child(3)')[0].text)

    #print(player_list)

    player_data_dict={}
    for p2 in player_list:
        url2 = 'https://maplestory.nexon.com/Ranking/World/Total?c='
        req2 = requests.get(url2 + p2)
        #print (url2+ p2)

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
            print(p2+ level[0].text)

            print(character[0].text)
            data = []

            if level==None:
                level[0].text = ""
            data.append(level[0].text)
            data.append(character[0].text)
            data.append(avatarImgSrc[0].text)
            player_data_dict[p2] = data

    return player_data_dict    

if __name__ =='__main__':
    print(len("https://avatar.maplestory.nexon.com/Character/LLPBHBDBGBEPEBNIGGJDEKLECENJGBKCAFMOFDAHMKMOLFEIONPFBDAHHLNNIFCAOAJMPKGFFPCBLKJJEGGAKNAIMOLKLOCKPCJMKKPOIOAMJLPOMNGAMCNDBGIDLEMFHDJHMGDBAMPGIGNBOLCIBJCOKFFIJPIFMDNCPFDFKFJHGPINLFDEBMCCDMBHCJMIGJCFJFDEFODIHNHBEGFJPENIGJJKKFPPGDEJOFBBEACCGFHMGPGKBNKJINFCNMCI.png"))
    player_data_dict = parse_guild_players()
    for p, d in player_data_dict.items():
        playerdata = PlayerData
        PlayerData(imgSrc = d[2], name = p, character = d[1],level = d[0]).save()



        '''
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
