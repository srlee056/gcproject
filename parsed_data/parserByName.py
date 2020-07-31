

import requests
from bs4 import BeautifulSoup
import json
import os


## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gcsite.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()
from django.shortcuts import get_object_or_404
from .models import PlayerData,Party

def parse_by_name(name):
    
        player = PlayerData()
        url2 = "https://maple.gg/u/"
        req2 = requests.get(url2 + name)

        html2 = req2.text
        soup2 = BeautifulSoup(html2, 'html.parser')

        avatarImgSrc= soup2.select(
            '#user-profile > section > div > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img'
        )
        character = soup2.select(
            '#user-profile > section > div > div.col-lg-8 > div.user-summary > ul > li:nth-child(2)'
            )
        ch = character[0].text
        
        level = soup2.select(
            '#user-profile > section > div > div.col-lg-8 > div.user-summary > ul > li:nth-child(1)'
            )
        lv = level[0].text
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
        player.imgSrc = avatarImgSrc[0]['src']
        player.name = name
        player.level = lv
        player.character = ch
        player.mrFloor = mrFloor
        player.party = get_object_or_404(Party, pk=0)
        player.save()
        return player
        
