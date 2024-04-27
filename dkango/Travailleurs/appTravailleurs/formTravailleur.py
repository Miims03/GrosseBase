from django import forms
from .models import Travailleur

class formTravailleur(forms.ModelForm):
    class Meta:
        model = Travailleur
        fields = ['name', 'salaire' , 'email']
