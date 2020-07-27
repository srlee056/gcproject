from django.urls import path
from . import views

urlpatterns = [
    path('', views.guild_player_list, name='player'),

]