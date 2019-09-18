from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import User_details
from django.core.exceptions import ObjectDoesNotExist
from .forms import detailsForm

def user_logout(request):
    if request.method == 'POST':
        logout(request)

    return redirect('base:home')


def user_profile(request):

    return render(request, 'accounts/profile.html', {})

def details(request):
    if request.method == 'POST':
        form = detailsForm(request.POST)

        if form.is_valid():

            usr_details = User_details()
            usr_details.user_name = form.user_name
            usr_details.user_gender = form.user_gender
            usr_details.description = form.description
            usr_details.user_user = request.user
            usr_details.save()

            return HttpResponse()

    else:
            form = detailsForm()
    return render(request,'accounts/details.html',{'form':form})
