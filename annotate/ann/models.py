from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TestModel(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        default_permissions = ('change', 'add', 
        'view')

# # Create your models here.
