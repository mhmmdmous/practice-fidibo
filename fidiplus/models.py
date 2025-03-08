from django.db import models
from django.utils import timezone  


class Users(models.Model):
    name = models.CharField(max_length= 20)
    national_ID = models.CharField(max_length=10 , unique= True)
    phone = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(null = True, blank= True)

    
    
    




