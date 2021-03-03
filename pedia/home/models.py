from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    # user = models.ForeignKey(User, on_delete= models.CASCADE,null= True)
    author = models.ForeignKey('auth.user', on_delete= models.CASCADE,null= True)
    name = models.CharField(max_length=56, null = True)
    Earlylife = models.TextField()
    Eduction = models.TextField()
    Intrest = models.TextField()
    Favorates = models.TextField()