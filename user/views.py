from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse
from user.forms import *
from user.models import *
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect


class AccountView(DetailView):
    model = User
    template_name = "account.html" 

def loginProfile(req):
    if req.method == "POST":
        form = ProfileLoginForm(req.POST)
        if form.is_valid():
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            profile = Profile.objects.get(phone=phone)
            if profile.user.check_password(password):
                login(req, profile.user)
                return redirect(reverse("account", args=[profile.user.id,]))
            return redirect(reverse("login"))
    else:
        form = ProfileLoginForm()
    return render(req, "login.html", {"form": form})
def registerProfile(req:HttpRequest):
    if req.method == "POST":
        form = ProfileRegisterForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]
            username = name + "/" + surname + "/" + last_name + "/" + phone
            if role == "EMP":
                user = User(username=username, first_name=surname, last_name=last_name)
                user.set_password(password)
                user.save()
                user.profile.phone = phone
                user.profile.role = True
                user.save()
            else:
                user = User(username=name, first_name=surname, last_name=last_name)
                user.set_password(password)
                user.save()
                user.profile.phone = phone
                user.profile.role = False
                user.save()
            return redirect(reverse("login"))
    else:
        form = ProfileRegisterForm()

    return render(req, "registration.html", {"form": form})


class UserLogoutView(LogoutView):
    pass
