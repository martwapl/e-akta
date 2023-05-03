from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label="Użytkownik", max_length=128)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)
