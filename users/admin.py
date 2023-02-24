from django.contrib import admin
from .models import Cart, Product, Order, Category

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'product_price')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','product_name', 'total_price')

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name', 'created_at')
