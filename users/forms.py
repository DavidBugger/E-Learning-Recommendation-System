from typing import Self
from django import forms 
from .models import Location 
from localflavor.us.models import USStateField, USZipCodeField

class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(blank=False)
    # def clean_zip_code():
    #     zip_code = Self.cleaned_data['zip_code']
    #     if not zip_code:
    #         raise forms.ValidationError('Zip Code is required')
    #     return zip_code
    
    class Meta:
        model = Location
        fields = {'address_1', 'address_2', 'city', 'state', 'zip_code'}
    