from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=20)
    pokedex = models.IntegerField()
    
    