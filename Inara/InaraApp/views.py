from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Commander, Ships, Station
from .forms import ShipsForm, StationForms, CommanderForm
# Create your views here.



def index(request):
    return render(request, 'index.html')

def add_commander(request):
    if request.method == 'POST':
        my_form = CommanderForm(request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data
            commander = Commander(name = data['name'].capitalize(), fleet = data['fleet'])
            commander.pub_date = datetime.now()
            commander.save()
            return redirect('index')
    else:
        my_form = CommanderForm()
        return render(request, 'add_commander.html', {'my_form':my_form})

def add_ships(request):
    if request.method == 'POST':
        # my_form = ShipsForm(request.POST, request.FILES)
        # if my_form.is_valid():
        #     data = my_form.cleaned_data
        #     ship = Ships(make = request.POST['make'].capitalize(), model = request.POST['model'].capitalize(), img=request.FILES, location = request.POST['location'])
        form = ShipsForm(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        my_form = ShipsForm()
        return render(request, 'add_ships.html', {'my_form':my_form})

def add_station(request):
    if request.method == 'POST':
        my_form = StationForms(request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data
            station = Station(name = data['name'].capitalize(), type = data['type'], system = data['system'].capitalize())
            station.save()
            return redirect('index')
        
    else:
        my_form = StationForms()
        return render(request, 'add_station.html', {'my_form':my_form})
    
class Staition_List(ListView):
    model = Station
    template_name = 'station_list.html'
    context_object_name = 'stations'
    
class Station_Detail(DetailView):
    model = Station
    template_name = 'station_detail.html'
    context_object_name = 'station'
    
class Ships_List(ListView):
    model = Ships
    template_name = 'ship_list.html'
    context_object_name = 'ships'
    
class Ship_Detail(DetailView):
    model = Ships
    template_name = 'ship_detail.html'
    context_object_name = 'ship'
    
    
class Commander_List(ListView):
    model = Commander
    template_name = 'commander_list.html'
    context_object_name = 'commanders'
    
class Commander_Detail(DetailView):
    model = Commander
    template_name = 'commander_detail.html'
    context_object_name = 'commander'
    
def search_commander(request):
    
    return render(request, 'search_commander.html')

def search(request):
    name = request.GET['commander'].capitalize()
    commander = Commander.objects.get(name=name)
    return render(request, 'search.html', {'commander':commander})