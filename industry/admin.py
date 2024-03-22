from django.contrib import admin
from industry.models import Category, Product, LeaveMessage

# Register your models here.

admin.site.site_header = '丰迪机械后台管理系统'
admin.site.site_title = '丰迪机械后台管理系统'


@admin.register(Category)
class CategoryManager(admin.ModelAdmin):
    list_display = ('id', 'category', 'is_active')
    list_display_links = ['category']
    list_editable = ['is_active']
    list_filter = ['category', 'is_active']
    list_per_page = 20


@admin.register(Product)
class ProductManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ['name']
    list_filter = ['name', 'category']


@admin.register(LeaveMessage)
class LeaveMessageManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'place')
    readonly_fields = ('id', 'name', 'email', 'phone', 'ipAddr', 'place', 'message')
    list_display_links = ['name']
    list_filter = ['name', 'place']
