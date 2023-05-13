from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import Case, File

from .models import *

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label="Użytkownik", max_length=128)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'description', 'case']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nazwa pliku"
        self.fields['file'].label = "Plik: (dozwolony typ: pdf)"
        self.fields['description'].label = "Opis"
        self.fields['case'].label = "Identyfikator sprawy"


class AddCaseForm(forms.ModelForm):

    class Meta:
        model = Case
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nazwa sprawy"
        self.fields['number'].label = "Numer sprawy"
        self.fields['description'].label = "Opis sprawy"
        self.fields['status'].label = "Stan sprawy"
        self.fields['category'].label = "Kategoria sprawy"

class FileDeleteForm(forms.ModelForm):

    class Meta:
        model = File
        fields = "__all__"

class CaseUpdateFormSU(forms.ModelForm):

    class Meta:
        model = Case
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nazwa sprawy"
        self.fields['number'].label = "Numer sprawy"
        self.fields['description'].label = "Opis sprawy"
        self.fields['status'].label = "Stan sprawy"
        self.fields['category'].label = "Kategoria sprawy"
        self.fields['user'].label = "Nazwa użytkownika"

class CaseUpdateForm(forms.ModelForm):

    class Meta:
        model = Case
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nazwa sprawy"
        self.fields['number'].label = "Numer sprawy"
        self.fields['description'].label = "Opis sprawy"
        self.fields['status'].label = "Stan sprawy"
        self.fields['category'].label = "Kategoria sprawy"

