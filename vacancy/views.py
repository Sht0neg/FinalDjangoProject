from django.shortcuts import render
from vacancy.models import *
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse
from django.urls import reverse

class IndexListView (ListView):
    model = Vacancy
    template_name = "catalog.html"
    context_object_name = "vacancies"

def catalog(req):
    vacancies = Vacancy.objects.all()
    return render(req, "catalog.html", {"vacancies": vacancies})



