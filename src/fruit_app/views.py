from django.shortcuts import render

from .models import Fruit

from .forms import FruitForm
# Create your views here.

def front_page_view(request):
    return render(request, "front-page.html")

def fruits_home_view(request):
    queryset = Fruit.objects.all()
    context = {
        "fruits": queryset
    }
    return render(request, "home.html", context)

def fruit_detail_view(request, id): 

    fruit = Fruit.objects.get(id= id)
    context = {
        "fruit": fruit
    }

    return render(request, "details.html", context)

def fruit_create_view(request):
    form = FruitForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        "fruit_form" : form
    }

    return render(request, 'create.html', context)