from django import forms
from .models import myStudents


class formulaireStudents(forms.ModelForm):
    class Meta:
        model=myStudents
        fields=['name','age','bourse']