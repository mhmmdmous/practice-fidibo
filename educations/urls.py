from django.urls import path 
from .views import educations

urlpatterns = [
    path('', educations)
]