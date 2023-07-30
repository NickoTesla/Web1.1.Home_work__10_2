from django.db import models
from django import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)