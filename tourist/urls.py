from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    
    path('tourist/', TouristAPIView.as_view()),
    path('tourist/<str:pk>/', TouristAPIView.as_view()),
   
] 
urlpatterns = format_suffix_patterns(urlpatterns)