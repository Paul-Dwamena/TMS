from django.db import models
from tourist.models import *



# Create your models here.


class Payment(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    tourist_id=models.ForeignKey(Tourist,on_delete=models.CASCADE,null=True)
    SITE_TYPES = (
        ('zoo', 'zoo'),
        ('fish_pond', 'fish pond'),
        ('culture','culture')
     
    )
    site = models.CharField(max_length=50, null=False, choices=SITE_TYPES, default="zoo")
    amount_paid=models.FloatField(default=0.0)
    date=models.DateField(auto_now_add=True)

    
