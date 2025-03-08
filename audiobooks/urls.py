from django.urls import path
from .views import audiobooks

urlpatterns = [
    path ('audiobooks', audiobooks)
]