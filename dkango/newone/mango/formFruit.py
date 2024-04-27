from django import forms
from .models import Fruit

class formFruit(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = [
            'name',
            'region',
            'image'
        ]