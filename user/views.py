from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse


class UserLoginView(LoginView):
    pass

class RegistrationView(CreateView):
    pass

class AccountView(DetailView):
    pass

class UserLogoutView(LogoutView):
    pass
