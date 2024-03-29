from django import forms 
from .models import Listing 

class ListingForm(forms.ModelForm):
    class Meta:
        image = forms.ImageField()
        model = Listing
        fields = {'brand', 'model', 'vin', 'mileage', 'color', 'description', 'engine', 'transmission', 'image'}