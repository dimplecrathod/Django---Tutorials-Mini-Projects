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

#Documentation for aggregation
#https://docs.djangoproject.com/en/2.0/topics/db/aggregation/