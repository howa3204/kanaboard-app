from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    date = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    def __str__(self):
        return str(self.title)
