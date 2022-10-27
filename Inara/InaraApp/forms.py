from django import forms
from django import forms
from django.forms import RadioSelect
from .models import STATION_CHOICES, Ships, Station

SATION_CHOICES = [
    ('CORIOLIS', 'Coriolis'),
    ('ORBITAL', 'Orbital'),
    ('REFINERY', 'Refinery'),
]

class CommanderForm(forms.Form):
    name = forms.CharField(max_length = 30)
    img = forms.ImageField()
    fleet = forms.ModelChoiceField(queryset=Ships.objects.all())
    
class ShipsForm(forms.Form):
    make = forms.CharField(max_length = 30)
    model = forms.CharField(max_length = 30)
    img = forms.ImageField()
    location = forms.ModelChoiceField(queryset=Station.objects.all())
    
class StationForms(forms.Form):
    name = forms.CharField(max_length = 30)
    type = forms.CharField(widget=forms.Select(choices=STATION_CHOICES))
    system = forms.CharField(max_length = 30)