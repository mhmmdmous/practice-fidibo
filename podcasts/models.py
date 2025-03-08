from django.db import models


class Narrator(models.Model):
    name = models.CharField(max_length= 20)
    national_ID = models.CharField(max_length= 10, unique=True)
    phone = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(null = True, blank= True)


class Guests(models.Model):
    name = models.CharField(max_length= 20)
    national_ID = models.CharField(max_length= 10, unique=True)
    phone = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(null = True, blank= True)


class Publisher(models.Model):
    name = models.CharField(max_length=20)
    national_id = models.CharField(max_length= 10, unique= True)
    establishment = models.DateField()
    email = models.EmailField()


class Podcast(models.Model):
    name = models.CharField(max_length= 20)
    channel_ID = models.CharField(max_length=20, unique= True)
    narrator = models.ForeignKey(to = Narrator, on_delete= models.PROTECT, related_name= 'narrator')
    guests = models.ManyToManyField(Guests)
    
    