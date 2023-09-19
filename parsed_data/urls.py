from django.urls import path
from . import views

app_name = 'guild'
urlpatterns = [
    path("", views.party_manager, name='player'),
    path("guildPlayerList/", views.guildPlayerList, name='player'),

    path('<int:player_id>/', views.detail, name = 'detail'),

    path('<int:player_id>/vote/', views.vote, name='vote'),

    path('<int:player_id>/delete/', views.delete, name='delete'),

    path('create/', views.create, name='create'),
    path('createByName/', views.createByName, name='createByName'),

    path('add/', views.add, name='add'),
    path('addByName/', views.addByName, name='addByName'),

    path('changeParty/', views.changeParty, name='changeParty')

    

]