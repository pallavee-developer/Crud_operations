from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    mobile = models.CharField(max_length=10)
    password= models.CharField(max_length=256)

