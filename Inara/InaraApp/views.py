from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Commander, Ships, Station
from .forms import ShipsForm, StationForms, CommanderForm
# Create your views here.



def index(request):
    return render(request, 'index.html')

def add_commander(request):
    if request.method == 'POST':
        my_form = CommanderForm(request.POST)
        if my_form.is_valid():
            data = my_form.clean_data
            commander = Commander(name = data['name'], pub_date = data['pub_date'], img = data['img'], fleet = data['fleet'])
            commander.save()
            return redirect('index')
        else:
            my_form = CommanderForm()
            return render(request, 'add_commander.html', {'my_form':my_form})

def add_ships(request):
    if request.method == 'POST':
        my_form = ShipsForm(request.POST, request.FILES)
        if my_form.is_valid():
            data = my_form.cleaned_data
            ship = Ships(make = data['make'].capitalize(), model = data['model'].capitalize(), img = data['img'], location = data['location'])
            ship.save()
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