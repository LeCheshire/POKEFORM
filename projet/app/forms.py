from django import forms
from .models import Pokemon

class PokeForm(forms.ModelForm):
    class Meta:
        
        model = Pokemon
        
        fields = ['name', 'type', 'lvl']