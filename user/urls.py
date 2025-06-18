from django.urls import path
from user.views import *

urlpatterns = [
    path("login/", loginProfile, name="login"),
    path("registration/", registerProfile, name="registration"),
    path("account/<int:pk>/", account, name="account"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
