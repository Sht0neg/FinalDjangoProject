from django.contrib import admin
from django.urls import path, include
from vacancy.views import *

urlpatterns = [
    path("catalog/", catalog, name="catalog"),
    path("<int:pk>", vacancy_card, name="vacancy"),
]