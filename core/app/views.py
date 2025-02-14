from django.shortcuts import render
from .models import Car, Category, Color

def home_page(request):
    cars = Car.objects.all()
    return render(request, 'app/index.html', {'cars': cars})
