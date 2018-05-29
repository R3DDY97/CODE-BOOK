
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as user_login
# from .models import Users, Registered

from .forms import RegisterForm


def index(request):
    return render(request, "user/index.html")


def login(request):
    return render(request, "registration/login.html")


def logout(request):
    return render(request, "registration/logout.html")


def register(request):
    form = RegisterForm(request.POST)
    print(form.is_valid())
    if request.method == 'POST' and form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        new_user = authenticate(username=username, password=raw_password)
        user_login(request, new_user)
        return redirect("index")
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


# def register(request):
#     form = UserCreationForm(request.POST)
#     print(form.is_valid())
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         username = form.cleaned_data['username']
#         raw_password = form.cleaned_data['password1']
#         new_user = authenticate(username=username, password=raw_password)
#         user_login(request, new_user)
#         return redirect("index")
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)
