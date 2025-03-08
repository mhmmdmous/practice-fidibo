from django.urls import path
from .views import ebooks

urlpatterns = [
    path ('ebooks', ebooks)
    
]
