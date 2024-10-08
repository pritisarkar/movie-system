from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    useremail = models.CharField(max_length = 50)
    password = models.CharField()
    def __str__(self):
        return self.name

class Genra(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

class Movie(models.Model):
    movie_name = models.CharField(max_length = 50)
    descrption = models.CharField(max_length=500)
    image = models.URLField()
    genre = models.CharField(max_length = 100)








