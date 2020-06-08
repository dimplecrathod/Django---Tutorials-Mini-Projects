from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20, default='DEFAULT_VALUE')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    creator = models.CharField(max_length=20, default='DEFAULT_VALUE')
    paradigm = models.CharField(max_length=20, default='DEFAULT_VALUE')

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default='18')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name


