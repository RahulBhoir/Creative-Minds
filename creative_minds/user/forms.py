from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']
