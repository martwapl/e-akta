from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import Case, File, Event, SendEmail


class LoginForm(forms.Form):

    username = forms.CharField(label="Użytkownik", max_length=128)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Użytkownik"
        self.fields['email'].label = "E-mail"
        self.fields['email'].required = True
        self.fields['first_name'].label = "Imię"
        self.fields['last_name'].label = "Nazwisko"
        self.fields['password1'].label = "Hasło"
        self.fields['password2'].label = "Powtórz hasło"


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'description', 'case']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)
        self.fields['name'].label = "Nazwa pliku"
        self.fields['file'].label = "Plik: (dozwolony typ: pdf)"
        self.fields['description'].label = "Opis"
        self.fields['case'].label = "Identyfikator sprawy"
        self.fields['case'].queryset = Case.objects.filter(user_id=user)


class AddCaseForm(forms.ModelForm):

    class Meta:
        model = Case
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nazwa sprawy"
        self.fields['description'].label = "Opis sprawy"
        self.fields['status'].label = "Stan sprawy"
        self.fields['category'].label = "Kategoria sprawy"
        self.fields['mail'].label = "E-mail klienta"


class FileDeleteForm(forms.ModelForm):

    class Meta:
        model = File
        fields = "__all__"


class CaseUpdateFormSU(forms.ModelForm):

    class Meta:
        model = Case
        fields = '__all__'

    def __init__(self, groups, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)
        self.fields['name'].label = "Nazwa sprawy"
        self.fields['description'].label = "Opis sprawy"
        self.fields['status'].label = "Stan sprawy"
        self.fields['category'].label = "Kategoria sprawy"
        self.fields['user'].label = "Nazwa użytkownika"
        self.fields['user'].queryset = User.objects.filter(groups=groups.id)
        self.fields['mail'].label = "Adres email klienta"


class AddEventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Nazwa zdarzenia"
        self.fields['start'].label = "Data i godzina rozpoczęcia"\
                                     "(format: YYYY-M-D H:M," \
                                     " np 2023-6-1 14:00)"
        self.fields['end'].label = "Data i godzina zakończenia"\
                                   "(format: YYYY-M-D H:M," \
                                   " np 2023-6-1 14:00)"


class EmailForm(forms.ModelForm):

    class Meta:
        model = SendEmail
        fields = ['recipient', 'subject']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipient'].label = "Adresat"
        self.fields['subject'].label = "Temat"
