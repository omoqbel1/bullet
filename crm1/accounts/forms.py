from django.forms import ModelForm
from .models import Customer
from django.db import models
from django.forms import ModelForm, DateInput


class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email', 'origin', 'destination', 'date', 'commodity']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
