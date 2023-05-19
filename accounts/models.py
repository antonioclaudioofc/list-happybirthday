import re
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Usuário', max_length=30, unique=True, validators=[validators.RegexValidator(re.compile(
        '^[\w.@+-]+$'), 'O nome do usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')])
    name = models.CharField('Nome', max_length=120, blank=True)
    email = models.EmailField('Email', unique=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self) -> str:
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Birthdays(models.Model):
    nome = models.CharField('Nome', max_length=120, blank=False)
    data_nascimento = models.TimeField('Data de nascimento', blank=False)
    notificar_por_email = models.BooleanField(
        'Notificar?', blank=True, default=True
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = 'Aniversariante'
        verbose_name_plural = 'Aniversariantes'
