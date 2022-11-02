from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('add-commander/', views.Add_Commander.as_view(), name='add_commander'),
    path('add-ships/', views.add_ships, name='add_ships'),
    path('add-station/', views.add_station, name='add_station'),
    path('station-list/', views.Station_List.as_view(), name='station_list'),
    path('station-detail/<pk>', views.Station_Detail.as_view(), name='station_detail'),
    path('ship-list/', views.Ships_List.as_view(), name='ship_list'),
    path('ship-detail/<pk>', views.Ship_Detail.as_view(), name='ship_detail'),
    path('commander-list/', views.Commander_List.as_view(), name='commander_list'),
    path('commander-detail/<pk>', views.Commander_Detail.as_view(), name='commander_detail'),
    path('search-commander/', views.search_commander, name='search_commander'),
    path('search/', views.Search.as_view(), name='search'),
    path('login/', views.login_user, name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
htmx_views = [
    path('check_username/', views.check_username, name='check_username'),
]

urlpatterns+=htmx_views