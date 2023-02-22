from django.contrib import admin
from .models import Cart, Product

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'product_price')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

