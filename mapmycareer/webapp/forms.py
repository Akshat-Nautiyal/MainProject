from django import forms
from .models import webinar

class MyForm(forms.ModelForm):
    name = forms.CharField(max_length=15)
    email = forms.TextField(max_length=20)
    phone = forms.IntegerField(max_length=20)
    city = forms.CharField(max_length=15)
    profession = forms.CharField(max_length=15)

    class Meta:
        model = webinar
        exclude = ()

