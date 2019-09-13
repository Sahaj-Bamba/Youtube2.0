from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import User_details
from django.core.exceptions import ObjectDoesNotExist


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Project_Allotment_Portal:home')
    else:
        form = UserCreationForm()
    return render(request,'Account/signup.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            try:
                temp = User_details.objects.get(user_user=user)
                request.session['gamer_type'] = temp.type
                request.session['gamer_authority'] = temp.authority
            except ObjectDoesNotExist:
                pass
            login(request, user)
            return redirect('base:home')
    else:
        form = AuthenticationForm()
    return render(request, 'Account/login.html', {'form': form})


def user_logout(request):
    if request.method == 'POST':
        logout(request)

    return redirect('base:home')


def user_profile(request):

    details = {}
    x = User_details.objects.get(user_user=request.user)
    details['Name'] = x.user_name
    details['CPI'] = x.user_cpi
    details['Gender'] = x.user_gender
    details['Regestration Number'] = x.user_reg_no
    details['Year'] = x.year
    return render(request, 'Account/profile.html', {'details': details})

