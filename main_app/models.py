from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    info = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=150)
    speakers = models.IntegerField()
    family = models.CharField(max_length=150)
    script = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    flag = models.CharField(max_length=250)
    info = models.TextField(max_length=500)
    population = models.IntegerField()
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name="countrys")
    languages = models.ManyToManyField(Language)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']



