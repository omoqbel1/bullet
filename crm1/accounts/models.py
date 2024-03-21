from django.db import models
from django.forms import ModelForm, DateInput

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    date = models.DateField()
    commodity = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.email} {self.origin} {self.destination} {self.date} {self.commodity}'
