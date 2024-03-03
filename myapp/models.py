from django.db import models

# Create your models here.

class Feature(models.Model):   # database named Feature is created
    name = models.CharField(max_length=100)
    details = models.CharField(max_length = 500)