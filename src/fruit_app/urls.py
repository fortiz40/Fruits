from django.contrib import admin
from django.urls import path, include

from .views import (
    fruit_detail_view, 
    fruits_home_view, 
    fruit_create_view,
    fruit_delete_view
    )

urlpatterns = [
    path('', fruits_home_view, name="fruits_home"),
    path('create/', fruit_create_view, name= "fruit_create"),
    path('<int:id>/details', fruit_detail_view, name= "fruit_detail"),
    path('<int:id>/delete', fruit_delete_view, name="fruit_delete"),
]