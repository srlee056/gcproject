from django.db import models

# Create your models here.
class PlayerData(models.Model):
    imgSrc = models.CharField(max_length=400)
    name = models.CharField(max_length=200)
    character = models.CharField(max_length=200)
    level = models.CharField(max_length=200)