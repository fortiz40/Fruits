from django import forms

from .models import Fruit

# class FruitForm(forms.Form):
#     name = forms.CharField()
#     description = forms.Textarea()
#     price = forms.DecimalField(decimal_places= 2)
#     image = forms.FileField()

class FruitForm(forms.ModelForm):
    
    class Meta:
        model = Fruit  
        fields = [
            'name',
            'description',
            'price',
            'image'
        ]
        widgets = {
            'description' : forms.Textarea(attrs = {'rows': 1})
        }

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

