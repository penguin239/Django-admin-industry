from django.contrib import admin
from industry.models import UserInfo, Category

# Register your models here.

admin.site.site_header = '工业管理系统'
admin.site.site_title = '后台管理系统'


@admin.register(UserInfo)
class UserInfoManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'age', 'account', 'password')
    list_display_links = ['name']


@admin.register(Category)
class CategoryManager(admin.ModelAdmin):
    list_display = ('id', 'category', 'is_active')
    list_display_links = ['category']
    list_editable = ['is_active']
    list_filter = ['category', 'is_active']
    list_per_page = 20
