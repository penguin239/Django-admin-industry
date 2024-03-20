from django.db import models


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


class LeaveMessage(models.Model):
    name = models.CharField(max_length=64, verbose_name='姓名')
    email = models.CharField(max_length=64, verbose_name='邮箱')
    phone = models.CharField(max_length=64, verbose_name='手机号')
    ipAddr = models.CharField(max_length=32, verbose_name='IP地址')
    place = models.CharField(max_length=255, verbose_name='用户地址')
    message = models.TextField(verbose_name='留言信息')
