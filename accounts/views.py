from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import RegisterBirthdays
from .models import Birthdays

def index(request):
    template_name = 'index.html'
    birthdays = Birthdays.objects.all()
    
    context = {
        'birthdays': birthdays
    }

    return render(request, template_name, context)


def register(request):
    template_name = 'register.html'
    context = {}

    if request.method == 'POST':
        form = RegisterBirthdays(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:index')
    else:
        form = RegisterBirthdays()

    context['form'] = form

    return render(request, template_name, context)


def profile(request):
    template_name = 'profile.html'

    return render(request, template_name)