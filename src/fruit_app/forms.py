from django import forms

from .models import Fruit

class FruitForm(forms.ModelForm):
    
    class Meta:
        model = Fruit  
        fields = [
            'name',
            'description',
            'price',
            'image'
        ]

class FruitDeleteForm(forms.ModelForm):
    
    class Meta:
        model = Fruit
        fields = []

class FruitUpdateForm(forms.ModelForm):

    class Meta:
        model=  Fruit
        fields = [
            'description',
            'price',
            'image'
        ]    

