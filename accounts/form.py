from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Birthdays

User = get_user_model()


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Usuário', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    name = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    image_profile = forms.ImageField(label='', required=False, widget=forms.ClearableFileInput(
        attrs={'type': 'file', 'class': 'form-control mt-3'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'A confirmação não está correta',
            )
        return password2

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'name', 'email']



class RegisterBirthdays(forms.ModelForm):
    name = forms.CharField(label='Nome', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(label='Data de nascimento', widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    image_birthdays = forms.ImageField(label='', required=False, widget=forms.ClearableFileInput(
        attrs={'type': 'file', 'class': 'form-control mt-3'}))

    class Meta:
        model = Birthdays
        fields = ['name', 'date_of_birth', 'image_birthdays']
