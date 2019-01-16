from django.db import models

# Create your models here.
class Animal(models.Model):
    title        = models.CharField(max_length=200)
    description  = models.TextField(null=True,default="A new Animal")
    image        = models.ImageField(blank=True,null=True)
    owner        = models.CharField(max_length=200)

