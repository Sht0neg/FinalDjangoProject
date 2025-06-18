from django.contrib import admin
from django.urls import path, include
from vacancy.views import *
from user.views import *

urlpatterns = [
    path("catalog/", catalog, name="catalog"),
    path("<int:pk>", vacancy_card, name="vacancy"),
    path("all-vacancies/", api_get_all_vacancies, name="api_get_all_vacancies"),
    path("create-vacancies/", create_vacancy, name="create_vacancy"),
    path("add-vacancy/<int:pk>", add_vacancy, name="add_vacancy"),
]