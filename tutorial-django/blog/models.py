from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # nuevo
    modified = models.DateTimeField(auto_now=True) # nuevo