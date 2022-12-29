from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    
    path('payment/', PaymentAPIView.as_view()),
    path('payment/<str:pk>/', PaymentAPIView.as_view()),
    path('payment-report/', get_tourist_report),
    path('payment-unpaid-report/', unpaid_tourist),
    path('payment-paid-report/', paying_tourist),
   
] 
urlpatterns = format_suffix_patterns(urlpatterns)