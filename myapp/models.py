from djongo import models

# Create your models here.

class Party(models.Model):
    title = models.CharField(max_length=100)


class Player(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    level = models.IntegerField()
