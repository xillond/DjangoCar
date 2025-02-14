from django.shortcuts import render
from .models import Car, Category, Color

def home_page(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})


def details_page(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'app/details.html', {'car': car})
