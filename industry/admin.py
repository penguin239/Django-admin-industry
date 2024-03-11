from django.contrib import admin
from industry.models import UserInfo

# Register your models here.

admin.site.site_header = '工业管理系统'
admin.site.site_title = '后台管理系统'


@admin.register(UserInfo)
class UserInfoManager(admin.ModelAdmin):
    list_display = ('name', 'sex', 'age', 'account', 'password')
