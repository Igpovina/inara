from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from .models import Commander, Ships, Station
from .forms import ShipsForm, StationForms, CommanderForm, RegisterForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.



def index(request):
    return render(request, 'index.html')

class Add_Commander(FormView):
    template_name="add_commander.html"
    form_class = CommanderForm
    success_url = '/InaraApp/commander-list/'
    
    def form_valid(self, form):
        commander = form.cleaned_data.get('name')
        ships = form.cleaned_data.get("fleet")

        fleet = Ships.objects.filter(model__in=ships)
        instance = Commander(name=commander.capitalize())
        instance.save()
        for ship in fleet:
            instance.fleet.add(ship)
        instance.save()

        return redirect('commander_list')


def add_ships(request):
    if request.method == 'POST':
        form = ShipsForm(data=request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect('ship_list')
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
            return redirect('station_list')
        
    else:
        my_form = StationForms()
        return render(request, 'add_station.html', {'my_form':my_form})
    
class Station_List(ListView):
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

class Search(ListView):
    model = Commander
    template_name = "search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("commander")
        if query=="":
            response = 'Commander not Found'
            HttpResponseRedirect('/InaraApp/', {'response':response})
        else:    
            object_list = Commander.objects.filter(Q(name__icontains=query))       
            return (object_list)
        
        
def login_user(request):
    if request.method == 'POST':
        my_form = AuthenticationForm(request, data=request.POST)
        if my_form.is_valid():
            data = my_form.cleaned_data
            user = data['username']
            pwd = data['password']
            
            user_auth = authenticate(username = user, password = pwd)
            
            if user_auth:
                login(request, user_auth)
                response = f'Welcome CMDR {user}'
                return render(request, 'index.html', {'response':response})
            else:
                response = 'User name or password are invalid'
                return render(request, 'index.html', {'response':response})
            
        response = 'User name or password are invalid'
        return render(request, 'inicio.html', {'response':response})
    else:
        my_form = AuthenticationForm()
        return render(request, 'login.html', {'my_form':my_form})
    
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def check_username(request):
    username = request.POST.get('username')
    print(username)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div style="color: red;"> This username already exists </div>')
    else:
        return HttpResponse('<div style="color: green;"> This username is available </div>')
