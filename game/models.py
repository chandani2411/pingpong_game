from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Refree(models.Model):
    name= models.CharField(max_length=225, default='Refree')
    winner= models.CharField(max_length=20, null=True, blank=True)
    scores= models.CharField(max_length=1500, null=True, blank=True)
    def __str__(self):
        return self.id

role_choices=(
    ('offensive','OFFENsIVE'),
    ('defensive','DEFENsIVE'),
    ('','')
)
# main_array=[1,2,3,4,5,6,7,8,9,10]

class Player(AbstractUser):
    player_id= models.IntegerField(null=True, blank=True)
    role= models.CharField(choices=role_choices, max_length=20)
    defencive_array_length= models.IntegerField(null=True, blank=True)
    defencive_array= models.CharField(max_length=16,blank=True, null=True)
    attacking_no=models.IntegerField(null=True, blank=True, max_length=1)
    points= models.IntegerField(default=0)
    joined= models.BooleanField(default=False)
    # refree= models.ForeignKey(Refree,on_delete=models.CASCADE, related_name='player', null=True, blank=True)



class Game(models.Model):
    gid=models.IntegerField(null=True, blank=True)
    round_winners=ArrayField(models.IntegerField(null=True, blank=True),blank=True, null=True)
