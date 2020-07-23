from django import forms

class createForm(forms.Form):
    img = forms.ImageField(label="photo")