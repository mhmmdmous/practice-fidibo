from django.urls import path
from .views import podcasts

urlpatterns = [
    path ('', podcasts)
    
]
