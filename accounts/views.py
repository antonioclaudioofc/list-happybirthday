from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .form import RegisterBirthdays
from .models import Birthdays

@login_required
def index(request):
    template_name = 'index.html'
    birthdays = Birthdays.objects.all()
    
    context = {
        'birthdays': birthdays
    }

    return render(request, template_name, context)

@login_required
def register(request):
    template_name = 'register.html'
    context = {}

    if request.method == 'POST':
        form = RegisterBirthdays(request.POST, request.FILES )
        if form.is_valid():
            register_birthday = form.save(commit=False)
            register_birthday.user = request.user
            register_birthday.save()
            form.save()
            return redirect('accounts:index')
    else:
        form = RegisterBirthdays()

    context['form'] = form

    return render(request, template_name, context)

@login_required
def profile(request):
    template_name = 'profile.html'

    return render(request, template_name)