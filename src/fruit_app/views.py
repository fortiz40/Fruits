from django.shortcuts import render

from .models import Fruit
# Create your views here.

def front_page_view(request):
    return render(request, "front-page.html")

def fruits_home_view(request):
    return render(request, "home.html", {})

def fruit_detail_view(request): 
    context = {}

    return render(request, "detail.html", context)
