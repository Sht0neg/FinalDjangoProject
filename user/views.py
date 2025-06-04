from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from user.forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        return reverse("account", args=[self.request.user.id,])

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "registration.html"

    def get_success_url(self):
        return reverse("login")

class AccountView(DetailView):
    model = User
    template_name = "account.html" 

def registerProfile(req):
    if req.method == "POST":
        form = ProfileRegisterForm(req.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = ProfileRegisterForm()

    return render(req, "registration.html", {"form": form})

class UserLogoutView(LogoutView):
    pass
