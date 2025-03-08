from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length= 20)
    national_ID = models.CharField(max_length= 10, unique=True)
    phone = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(null = True, blank= True)


class Users(models.Model):
    name = models.CharField(max_length= 20)
    national_ID = models.CharField(max_length= 10, unique=True)
    phone = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(null = True, blank= True)


class Publisher(models.Model):
    name = models.CharField(max_length=20)
    national_id = models.CharField(max_length= 10, unique= True)
    establishment = models.DateField()
    email = models.EmailField()


class Magazines(models.Model):
    name = models.CharField(max_length= 20)
    number = models.CharField(max_length=20, unique= True)
    authors = models.ManyToManyField(Authors, related_name= 'narrator')
    users = models.ManyToManyField(Users, related_name='users')
    price = models.IntegerField()
    
    