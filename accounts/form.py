from django import forms
from django.contrib.auth import get_user_model
from .models import Birthdays

User = get_user_model()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Usuário')
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError(
    #             'A confirmação não está correta',
    #         )
    #     return password2

    # def save(self, commit=True):
    #     user = super(RegisterForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])

    #     if commit:
    #         user.save()
    #     return user



    class Meta:
        model = User
        fields = ['username', 'name', 'email']
    # username = forms.CharField('Usuário', max_length=30, unique=True, 
    # name = forms.CharField('Nome', max_length=120, blank=True)
    # email = forms.EmailField('Email', unique=True)
    # created_at = forms.DateTimeField('Data de criação', auto_now_add=True)

class RegisterBirthdays(forms.ModelForm):
    nome = forms.CharField(label='Nome')
    data_nascimento = forms.DateField(label='Data de nascimento',widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Birthdays
        fields = ['nome', 'data_nascimento']