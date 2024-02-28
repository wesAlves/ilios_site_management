from django.db import models


# Create your models here.
class AvailableSite(models.Model):
    name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    atrributes = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    base_template = models.CharField(max_length=200)
    desctiption = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
