from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Party
# Create your views here.

def helloworld(request):
    return HttpResponse('hello world!')


def party_list(request):
    parties = Party.objects.all().values()
    players = Player.objects.all().values()
    return render (request, 'myapp/party_list.html',{'parties':parties, 'players':players})