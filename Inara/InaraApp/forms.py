from django import forms
from django import forms
from .models import STATION_CHOICES, Ships, Station


class CommanderForm(forms.Form):
    name = forms.CharField(max_length = 30)
    # pub_date = forms.DateField()
    fleet = forms.ModelChoiceField(queryset=Ships.objects.all())
    
class ShipsForm(forms.Form):
    make = forms.CharField(max_length = 30)
    model = forms.CharField(max_length = 30)
    location = forms.ModelChoiceField(queryset=Station.objects.all())
    
class StationForms(forms.Form):
    name = forms.CharField(max_length = 30)
    type = forms.CharField(widget=forms.Select(choices=STATION_CHOICES))
    system = forms.CharField(max_length = 30)