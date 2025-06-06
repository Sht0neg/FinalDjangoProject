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

def vacancy_card(request: HttpRequest, pk: int):
    if (pk):
        vacancy = Vacancy.objects.get(id=pk)
        return render(request, "vacancy_card.html", {"vacancy":vacancy})
    return reverse("catalog")

