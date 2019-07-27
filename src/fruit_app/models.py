from django.db import models

# Create your models here.
class Fruit(models.Model):
    
    name =  models.CharField(blank= False, max_length = 25) 
    description = models.TextField(blank= False, null= False)
    price = models.DecimalField(blank=False, decimal_places= 2, max_digits= 6)

    