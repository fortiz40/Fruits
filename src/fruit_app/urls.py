from django.contrib import admin
from django.urls import path, include

from .views import fruit_detail_view, fruits_home_view

urlpatterns = [
    path('', fruits_home_view, name="fruits_home"),
    path('detail', fruit_detail_view, name= "fruits-detail"),
]