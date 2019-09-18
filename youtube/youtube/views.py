from django.shortcuts import render
from .forms import detailsForm
from .models import User_details

def details(request):
    if request.method == 'POST':

    form = detailsForm(request.POST)
    if form.is_valid():

        usr_details = User_details()
        usr_details.user_name = from.user_name
        usr_details.user_gender = form.user_gender
        usr_details.description = form.description
        usr_details.user_user = request.user

        return HttpResponseRedirect('/thanks/')

    else:
        form = detailsForm()

    return render(request,'',{'form':form})
