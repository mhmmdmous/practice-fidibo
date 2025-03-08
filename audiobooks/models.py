from django.db import models


class Author(models.Model):
    name = models.CharField(max_length= 20)
    national_ID = models.CharField(max_length=10 , unique= True)
    phone = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(null = True, blank= True)


class Publisher(models.Model):
    name = models.CharField(max_length=20)
    national_id = models.CharField(max_length= 10, unique= True)
    establishment = models.DateField()
    email = models.EmailField()


class Narrator(models.Model):
    name = models.CharField(max_length= 20)
    national_ID = models.CharField(max_length= 10, unique=True)
    phone = models.CharField(max_length= 11, unique= True)
    email = models.EmailField(null = True, blank= True)



class Audiobooks(models.Model):
    name = models.CharField(max_length= 50)
    author = models.ForeignKey(to= Author, on_delete= models.CASCADE, related_name= 'author')
    narrator = models.ForeignKey(to = Narrator, on_delete= models.CASCADE, related_name='narrator')
    publisher = models.ForeignKey(to= Publisher, on_delete= models.CASCADE, related_name= 'publisher')
    price = models.CharField(max_length= 10)

