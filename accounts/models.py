import re

from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Usuário', max_length=30, unique=True, validators=[validators.RegexValidator(re.compile(
        '^[\w.@+-]+$'), 'O nome do usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')])
    email = models.EmailField('Email', unique=True)
    name = models.CharField('Nome', max_length=120, blank=False)
    image_profile = models.ImageField(upload_to='perfil/images', blank=True, null=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de criação', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.name 

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Birthdays(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=models.CASCADE, default=False)
    name = models.CharField('Nome', max_length=120, blank=False)
    date_of_birth = models.DateField('Data de nascimento', blank=False)
    notify_by_email = models.BooleanField(
        'Notificar?', blank=True, default=True
    ) 
    image_birthdays = models.ImageField(upload_to='perfil/images', blank=True, null=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Aniversariante'
        verbose_name_plural = 'Aniversariantes'
