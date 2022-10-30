from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add-commander/', views.add_commander, name='add_commander'),
    path('add-ships/', views.add_ships, name='add_ships'),
    path('add-station/', views.add_station, name='add_station'),
    path('', views.index, name='index'),
    path('station-list/', views.Staition_List.as_view(), name='station_list'),
    path('station-detail/<pk>', views.Station_Detail.as_view(), name='station_detail'),
    path('ship-list/', views.Ships_List.as_view(), name='ship_list'),
    path('ship-detail/<pk>', views.Ship_Detail.as_view(), name='ship_detail'),
    path('commander-list/', views.Commander_List.as_view(), name='commander_list'),
    path('commander-detail/<pk>', views.Commander_Detail.as_view(), name='commander_detail'),
    path('search-commander/', views.search_commander, name='search_commander'),
    path('search/', views.search, name='search'),
]
htmx_urlpatterns = [
    
]

urlpatterns += htmx_urlpatterns