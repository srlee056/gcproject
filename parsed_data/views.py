from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import PlayerData
from django.shortcuts import render, get_object_or_404
# Create your views here.

def guild_player_list(request):
    
    players = PlayerData.objects.order_by('character')
    return render (request, 'parsed_data/guild_player_list.html',{'players':players})

def detail(request, player_id):
    player=get_object_or_404(PlayerData, pk=player_id)
    return render(request, 'parsed_data/detail.html', {'player':player})

def vote(request, player_id):
    player=get_object_or_404(PlayerData, pk=player_id)
    
    
    player.name = request.POST['p_name']
    player.character = request.POST['p_character']
    player.level = pk=request.POST['p_level']
    player.save()

    return HttpResponseRedirect(reverse('guild:results', args = (player.id,)))
    
def results(request, player_id):
    player=get_object_or_404(PlayerData, pk=player_id)
    return render(request, 'parsed_data/results.html', {'player':player})
