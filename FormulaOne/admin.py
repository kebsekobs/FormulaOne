from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

import FormulaOne.models as models
from .forms import RegisterUserForm, LoginUserForm, ProfileForm, RaceForm
from .models import F1Drivers
from .models import F1StatsSoFar
from .models import Schedule
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(models.F1Drivers)
admin.site.register(models.F1StatsSoFar)
admin.site.register(models.Schedule)

from django.shortcuts import render, redirect


def home_link(request):
    return redirect('/drivers/all/')


def drivers_link(request, team="all"):
    if team == "all":
        drivers = F1Drivers.objects.all()
    elif team == "0":
        drivers = F1Drivers.objects.filter(team="Red Bull Racing")
    elif team == "4":
        drivers = F1Drivers.objects.filter(team="McLaren")
    elif team == "7":
        drivers = F1Drivers.objects.filter(team="Aston Martin Racing")
    elif team == "8":
        drivers = F1Drivers.objects.filter(team="Williams")
    elif team == "6":
        drivers = F1Drivers.objects.filter(team="AlphaTauri")
    elif team == "5":
        drivers = F1Drivers.objects.filter(team="Alpine")
    elif team == "3":
        drivers = F1Drivers.objects.filter(team="Ferrari")
    elif team == "2":
        drivers = F1Drivers.objects.filter(team="Haas F1 Team")
    elif team == "1":
        drivers = F1Drivers.objects.filter(team="Mercedes")
    elif team == "9":
        drivers = F1Drivers.objects.filter(team="Alfa Romeo")
    return render(request, 'driversPage.html', {'drivers': drivers})


def points_link(request):
    statistics = F1StatsSoFar.objects.order_by('-points')
    return render(request, 'points.html', {'statistics': statistics})


def schedule_link(request):
    schedule = Schedule.objects.order_by('round')
    return render(request, 'schedule.html', {'schedule': schedule})


def login(request):
    return HttpResponse("Авторизация")


def signin_link(request):
    return render(request, "signin.html")


def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request, "profile.html")


@login_required
def shop(request):
    error = ''
    if request.method == 'POST':
        form = RaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/schedule/')
        else:
            error = 'Скорее всего проблема с датой(('

    form = RaceForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, "shop.html", data)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    User._meta.get_field('email')._unique = True
    template_name = 'signin.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(user)
        return redirect('/login/')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'


class Profile(PasswordChangeView):
    form_class = ProfileForm
    template_name = 'profile.html'

    def form_valid(self, form):
        user = form.save()
        login(user)
        return redirect('/login/')


