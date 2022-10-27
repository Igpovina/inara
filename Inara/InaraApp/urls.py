from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add-commander', views.add_commander, name='add_commander'),
    path('add-ships', views.add_ships, name='add_ships'),
    path('add-station', views.add_station, name='add_station'),
    path('', views.index, name='index'),
]