from django.shortcuts import render

from .models import Fruit
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
    print(id)
    print()
    print()
    print()
    print()

    fruit = Fruit.objects.get(id= id)
    context = {
        "fruit": fruit
    }

    return render(request, "details.html", context)
