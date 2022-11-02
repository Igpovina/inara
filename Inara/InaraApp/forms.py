from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import STATION_CHOICES, Commander, Ships, Station, User


class CommanderForm(forms.ModelForm):
    # name = forms.CharField(max_length = 30)
    # # pub_date = forms.DateField()
    # fleet = forms.ModelMultipleChoiceField(ModelChoiceField.queryset.all())
    fleet = forms.ModelMultipleChoiceField(
    queryset=Ships.objects.all(),
    widget=forms.CheckboxSelectMultiple
  )
    class Meta:
        model = Commander
        fields = ('name', 'fleet')
        
    
class ShipsForm(forms.ModelForm):
    class Meta:
        model = Ships
        fields = ("make", "model", "img", "location")
    
class StationForms(forms.Form):
    name = forms.CharField(max_length = 30)
    type = forms.CharField(widget=forms.Select(choices=STATION_CHOICES))
    system = forms.CharField(max_length = 30)
    


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]