from django.shortcuts import render


def catalog(req):
    return render(req, "catalog.html")
# Create your views here.
