from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, Party
# Create your views here.

def helloworld(request):
    return HttpResponse('hello world!')

def party_list(request):
    return render (request, 'myapp/party_list.html',{})