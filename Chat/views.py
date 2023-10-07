from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterationForm
# Create your views here.

def Register(request):
    if request.method == "POST" :
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
    else:
        form = RegisterationForm()

    return render(request, "Chat/registration.html", {"form":form})
 