from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Home, VacantHome


# User Register form that requires user to input username, email, password and matching password confirmation
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Form for Homes that uses all fields based on the Home Model
class HomeDetailsForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = '__all__'


# Form for Vacant Homes that uses all fields based on the VacantHome Model
class VacantHomesForm(forms.ModelForm):

    class Meta:
        model = VacantHome
        fields = '__all__'
