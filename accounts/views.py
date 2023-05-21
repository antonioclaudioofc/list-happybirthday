from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import ResgisterBirthdays

# Create your views here.
def index(request):
    template_name = 'index.html'

    if request.method == 'POST':
        form = ResgisterBirthdays(request.POST)
    else:
        form = ResgisterBirthdays()

    context = {
        'form': form
    }

    return render(request, template_name, context)


def register(request):
    template_name = 'register.html'

    return render(request, template_name)

def profile(request):
    template_name = 'profile.html'

    return render(request, template_name)