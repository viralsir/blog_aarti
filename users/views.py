from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.views import
# Create your views here.

def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('register')
        else :
            return render(request, "users/register.html", {
                "form": form
            })

    return render(request,"users/register.html",{
        "form":form
    })