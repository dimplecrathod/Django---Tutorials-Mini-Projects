from django.db import models
from django.contrib.auth.models import User

class Example(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

class Programmer(models.Model):
    name= models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lang(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=20)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    location = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username