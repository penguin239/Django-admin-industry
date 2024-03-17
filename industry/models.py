from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=3)
    age = models.IntegerField()
    account = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class Category(models.Model):
    category = models.CharField(max_length=64, verbose_name='类别', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='启用')

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='机械名称')
    profile = models.TextField(verbose_name='产品介绍', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='类别')
    product_image = models.ImageField(verbose_name='产品图片', default=0)
    param_image = models.ImageField(verbose_name='参数图片', default=0, upload_to='param_img/')
    # todo: 为产品详细信息设计表
