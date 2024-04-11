from django.contrib import admin
from main.models import (
    Category, Product, NotificationCategory, NotificationProduct
)
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'price', 'created_at']
    search_fields = ['name', 'price']
    list_filter = ['created_at', 'category']



@admin.register(NotificationProduct)
class NotificationProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'product__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

@admin.register(NotificationCategory)
class NotificationCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username', 'category__name')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    

