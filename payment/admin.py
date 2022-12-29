from django.contrib import admin
from .models import *
# Register your models here.


class PaymentAdmin( admin.ModelAdmin):
    list_display = ('id','date','amount_paid','site','tourist_id')
   


admin.site.register(Payment,PaymentAdmin)