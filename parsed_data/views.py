from django.views import generic
from .models import PlayerData,Party

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, get_object_or_404

from . import parserByName
# Create your views here.


def guildPlayerList(request):
    
    UCPlayers = PlayerData.objects.filter(party_id=0).order_by('name') 
    return render (request, 'parsed_data/guildPlayerList.html',{'UCPlayers':UCPlayers})

def party_manager(request):
    
    playersList = []
    for i in range(1, 13) :
        p = PlayerData.objects.filter(party_id=i)
        playersList.append(p) 
    return render (request, 'parsed_data/party_manager.html',{'playersList':playersList, 'range': range(1,13)})

def detail(request, player_id):
    player=get_object_or_404(PlayerData, pk=player_id)
    return render(request, 'parsed_data/detail.html', {'player':player})


def changeParty(request):
    player=get_object_or_404(PlayerData, pk=request.POST['player_id'])
    pParty=get_object_or_404(Party, pk=request.POST['party_id'])
    player.party = pParty
    player.save()
    print("saved")
    return HttpResponseRedirect(reverse('guild:player'))

def vote(request, player_id):
    player=get_object_or_404(PlayerData, pk=player_id)
    pParty=get_object_or_404(Party, pk=request.POST['p_party'])
    #print(player.party.id)
    player.imgSrc = request.POST['p_imgSrc']
    player.name = request.POST['p_name']
    player.character = request.POST['p_character']
    player.level = request.POST['p_level']
    player.mrFloor = request.POST['p_mrFloor']
    player.party = pParty
    
    #print(player.party)
   
    player.save()
    #print(player)

    return HttpResponseRedirect(reverse('guild:player'))

def create(request):
    player = PlayerData(imgSrc="캐릭터 이미지 링크", name="이름", character="직업", level="레벨", mrFloor="무릉층수")
    
    return render(request, 'parsed_data/create.html', {'player':player})

def createByName(request):
    player = PlayerData(name="이름")
    
    return render(request, 'parsed_data/createByName.html', {'player':player})


def add(request):
    player=PlayerData()
    pParty=get_object_or_404(Party, pk=request.POST['p_party'])

    player.imgSrc = request.POST['p_imgSrc']
    player.name = request.POST['p_name']
    player.character = request.POST['p_character']
    player.level = pk=request.POST['p_level']
    player.mrFloor = pk=request.POST['p_mrFloor']
    player.party = pParty
    player.save()

    return HttpResponseRedirect(reverse('guild:player'))

def addByName(request):
    player = parserByName.parse_by_name(request.POST['p_name'])
    #player.save()

    return HttpResponseRedirect(reverse('guild:player'))


def delete(request, player_id):
    player=get_object_or_404(PlayerData, pk=player_id)
    player.delete()
    return HttpResponseRedirect(reverse('guild:player'))
