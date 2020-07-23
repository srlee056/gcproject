from django.db import models

# Create your models here.
class PlayerData(models.Model):
    imgSrc = models.URLField()
    name = models.CharField(max_length=200)
    character = models.CharField(max_length=200)
    level = models.IntegerField()