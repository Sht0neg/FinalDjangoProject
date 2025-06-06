from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from user.forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse("account", args=[self.request.user.id,])


class AccountView(DetailView):
    model = User
    template_name = "account.html" 

def registerProfile(req):
    if req.method == "POST":
        form = ProfileRegisterForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]
            if role == "EMP":
                user = User(username=name, first_name=surname, last_name=last_name)
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
