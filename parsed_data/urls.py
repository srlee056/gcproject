from django.urls import path
from . import views

app_name = 'guild'
urlpatterns = [
    path("", views.guild_player_list, name='player'),

    path('<int:player_id>/', views.detail, name = 'detail'),

    path('<int:player_id>/vote/', views.vote, name='vote'),

    path('<int:player_id>/delete/', views.delete, name='delete'),

    path('create/', views.create, name='create'),

    path('add/', views.add, name='add'),

    

]