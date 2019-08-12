from django.db import models

# Create your models here.

class Post(models.Model):
    imgName = models.CharField(max_length=144)
    title = models.CharField(max_length=144)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class People(models.Model):
    imgName = models.CharField(max_length=144)
    name = models.CharField(max_length=144)
    subname = models.CharField(max_length=144)
    title = models.CharField(max_length=144)
    content = models.TextField()
    short_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)