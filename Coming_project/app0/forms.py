from django import forms
from .models import item

class createForm(forms.Form):
    
    img = forms.ImageField(label="photo")
