from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import *


def home(request: WSGIRequest):
    brands = Brands.objects.all()
    cars = Cars.objects.all()
    context = {
        'brands': brands,
        'cars': cars
    }

    return render(request, 'index.html', context)

