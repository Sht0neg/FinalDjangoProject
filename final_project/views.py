from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from datetime import *
from vacancy.models import *

def main(req):
    return render(req, "main.html")

def info(req):
    return render(req, "info.html")