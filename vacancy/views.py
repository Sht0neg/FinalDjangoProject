from django.shortcuts import render
from vacancy.models import *
from vacancy.forms import *
from datetime import *
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from django.shortcuts import redirect

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
        vacancies = vacancies.filter(price__gt=int(price))
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

def create_vacancy(req):
    if req.method == "POST":
        form = CreateVacancyForm(req.POST)
        print(form.is_valid())
        if form.is_valid():
            print("fkld")
            title = form.cleaned_data["title"]
            desc = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            vacancy = Vacancy()
            vacancy.title = title
            vacancy.description = desc
            vacancy.price = price
            vacancy.publication_date = datetime.now()
            vacancy.author = req.user.profile
            vacancy.save()
            print(vacancy)
            return redirect(reverse("catalog"))
    else:
        form = CreateVacancyForm()

    return render(req, "create_vacancy.html", {"form": form})

def add_vacancy(req, pk:int):
    vacancy = Vacancy.objects.get(id=pk)
    profile = req.user.profile
    profile.submit_vacancies.add(vacancy)
    return redirect(reverse("account", args=[req.user.id,]))

def del_vacancy(req, pk:int):
    vacancy = Vacancy.objects.get(id=pk)
    profile = req.user.profile
    profile.submit_vacancies.remove(vacancy)
    return redirect(reverse("account", args=[req.user.id,]))

def api_get_all_vacancies(req):
    vacancies = Vacancy.objects.all()
    dataList = [vacancy.parse_object() for vacancy in vacancies]
    return JsonResponse(dataList, safe=False)
