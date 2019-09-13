from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import User_details
from django.core.exceptions import ObjectDoesNotExist


def user_logout(request):
    if request.method == 'POST':
        logout(request)

    return redirect('base:home')


def user_profile(request):

    return render(request, 'Account/profile.html', {})

