from django.conf import settings
from django.db import models

# Create your models here.

class Letter(models.Model):
    letter_title = models.CharField(max_length=200)
    letter_type = models.CharField(max_length=200)
    school_association = models.CharField(max_length=200, blank=True)
    author_prefix = models.CharField(max_length=200, blank=True)
    author_first_name = models.CharField(max_length=200)
    author_last_name = models.CharField(max_length=200)
    author_title = models.CharField(max_length=200, blank=True)
    organization_name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.letter_type)
