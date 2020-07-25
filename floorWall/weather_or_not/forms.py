from django.forms import ModelForm, TextInput
from .models import Geo

class GeoForm(ModelForm):
    class Meta:
        model = Geo
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'Geo Name'}),
        } #updates the input class to have the correct Bulma class and placeholder