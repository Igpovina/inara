from django import forms
from .models import STATION_CHOICES, Ships, Station


class CommanderForm(forms.Form):
    name = forms.CharField(max_length = 30)
    # pub_date = forms.DateField()
    fleet = forms.ModelChoiceField(queryset=Ships.objects.all())
    
class ShipsForm(forms.ModelForm):
    class Meta:
        model = Ships
        fields = ("make", "model", "img", "location")
    
class StationForms(forms.Form):
    name = forms.CharField(max_length = 30)
    type = forms.CharField(widget=forms.Select(choices=STATION_CHOICES))
    system = forms.CharField(max_length = 30)