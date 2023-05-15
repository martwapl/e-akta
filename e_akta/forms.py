from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
import datetime

from .models import Case, File, Event, Profile

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
        self.fields['case'].queryset = File.objects.values_list('name', flat=True)


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

class AddEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Nazwa zdarzenia"
        self.fields['start'].label = "Data i godzina rozpoczęcia (format: D/M/Y H/M, np 5/6/2023 14:00)"
        self.fields['end'].label = "Data i godzina zakończenia (format: D/M/Y H/M, np 5/6/2023 14:00)"
        self.fields['place'].label = "Miescowość/Sąd"