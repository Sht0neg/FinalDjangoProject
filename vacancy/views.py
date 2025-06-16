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
    price = req.GET.get("price")
    date = req.GET.get("date")
    title = req.GET.get("title")
    vacancies = Vacancy.objects.all()
    if (price):
        vacancies = vacancies.filter(price=int(price))
    if (date):
        vacancies = vacancies.filter(publication_date__month__gt=int(date) - 1) 
    if (title):
        vacancies = vacancies.filter(id=int(title))
    return render(req, "catalog.html", {"vacancies": vacancies, "price":price, "date":date, "title":Vacancy.objects.get(id=int(title)) if title else ""})

def vacancy_card(request: HttpRequest, pk: int):
    if (pk):
        vacancy = Vacancy.objects.get(id=pk)
        return render(request, "vacancy_card.html", {"vacancy":vacancy})
    return reverse("catalog")

def api_get_all_vacancies(req):
    vacancies = Vacancy.objects.all()
    dataList = [vacancy.parse_object() for vacancy in vacancies]
    return JsonResponse(dataList, safe=False)
