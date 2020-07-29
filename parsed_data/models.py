from django.db import models

# Create your models here.
class PlayerData(models.Model):
    imgSrc = models.CharField(max_length=400)
    name = models.CharField(max_length=200)
    character = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    mrFloor = models.CharField(max_length=200)
    
    party = models.ForeignKey(
        'Party',
        on_delete = models.CASCADE,
    )

class Party(models.Model):
    name = models.CharField(max_length=200)

'''
class mCharacter(models.Model):
    name = models.CharField(max_length=200)
    utilType= models.CharField(max_length=200)  # 파티뎀증, 수로뎀증 
    utilName = models.CharField(max_length=200) # 플위 장판, 메카닉 웨이버, 비숍 프레이, 하울링, 어블, 샤프아이즈 등등
'''

