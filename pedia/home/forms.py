from django import forms
from .models import Person

class Personforms(forms.ModelForm):
    class Meta:
        model =  Person
        fields = ['name','Earlylife','Eduction','Intrest','Favorates']