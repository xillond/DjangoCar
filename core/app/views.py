from django.shortcuts import render, redirect
from .models import Car, Category, Color
from .forms import CarCreateForm
from django.db.models import Q

def home_page(request):
    cars = Car.objects.all()
    if 'search' in request.GET:
        search = request.GET['search']
        cars = Car.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))

    return render(request, 'app/index.html', {'cars': cars})


def details_page(request, pk):
    car = Car.objects.get(id=pk)
    return render(request, 'app/details.html', {'car': car})

def add_car(request):

    colors = Color.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST['category_id']
        description = request.POST['description']
        title = request.POST['title']
        model = request.POST['model']
        year = request.POST['year']
        engine_capacity = request.POST['engine_capacity']
        odometer = request.POST['odometer']
        color_id = request.POST['color_id']
        image = request.FILES['image']

        color = Color.objects.get(id=color_id)
        category = Category.objects.get(id=category_id)

        new_car = Car(title=title, description=description, model=model,year=year,
                    engine_capacity=engine_capacity, odometer=odometer, color=color, category=category, image=image)
        new_car.save()
        return redirect('home')

    return render(request, 'app/add_car.html', {'colors': colors, 'categories': categories})


def add_car_django(request):

    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = CarCreateForm()
    return render(request, 'app/add_car_django.html', {'form':form})

