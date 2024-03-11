from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=3)
    age = models.IntegerField()
    account = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
