from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=3)
    age = models.IntegerField()
    account = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class Category(models.Model):
    category = models.CharField(max_length=64, verbose_name='类别')
    is_active = models.BooleanField(default=True, verbose_name='启用')


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='机械名称')
    category = models.CharField(max_length=64, verbose_name='类别')
