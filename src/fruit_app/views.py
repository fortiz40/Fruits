from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Fruit

from .forms import FruitForm, FruitDeleteForm, FruitUpdateForm
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
        return redirect("fruits_home")

    context = {
        "fruit_form" : form
    }

    return render(request, 'create.html', context)

def fruit_delete_view(request, id):
    fruit = None
    try:
        fruit = Fruit.objects.get(id = id)
    except:
        return redirect("fruits_home")
    form = FruitDeleteForm(request.POST or None) 

    if request.method == "POST":
        fruit.delete()
        return redirect("fruits_home")
    

    context = {
        "fruit" : fruit,
        "fruit_delete_form": form
    }

    return render(request, 'delete.html', context)

def fruit_update_view(request, id):

    fruit = Fruit.objects.get(id = id)
    form = FruitUpdateForm(request.POST or None, instance = fruit)

    if form.is_valid():
        fruit= form.save(commit = False)
        fruit.save()
        return redirect("fruit_detail", id= id)

    context = {
        'fruit': fruit,
        'fruit_form' : form 
    }

    return render(request, 'update.html', context)