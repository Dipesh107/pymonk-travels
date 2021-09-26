from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import bookedFlights
from .models import bookedTrains
from .models import bookedHotels
from .models import MyBookedFlights


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class afterbookForm(forms.ModelForm):
    class Meta:
        model = bookedFlights
        fields = ['name', 'email', 'mobile']


class afterbookFormTrains(forms.ModelForm):
    class Meta:
        model = bookedTrains
        fields = ['name', 'email', 'mobile']


class afterbookFormHotels(forms.ModelForm):
    class Meta:
        model = bookedHotels
        fields = ['name', 'email', 'mobile']


class myBookedFlights(forms.ModelForm):
    class Meta:
        model = MyBookedFlights
        fields = ['city_from', 'destination', 'name', 'email']
