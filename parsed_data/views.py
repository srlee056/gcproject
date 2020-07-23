from django.shortcuts import render
from .models import PlayerData
# Create your views here.

def player_list(request){
    players = PlayerData.objects.all.values()
    return render (request, 'parsed_data/player_list.html',{'players':players})

}