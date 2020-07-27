from django.shortcuts import render
from .models import PlayerData
# Create your views here.

def guild_player_list(request):
    
    players = PlayerData.objects.order_by('level')
    return render (request, 'parsed_data/guild_player_list.html',{'players':players})
