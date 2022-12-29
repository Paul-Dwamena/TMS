from django.contrib import admin
from .models import *
# Register your models here.


class TouristAdmin( admin.ModelAdmin):
    list_display = ('id','firstname','lastname')
   


admin.site.register(Tourist,TouristAdmin)