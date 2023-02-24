from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=True)

    def __str__(self):
        return f"{self.name}"



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.user.username} - $ "

    @property
    def product_name(self):
        return [product.name for product in self.products.all()]

    def product_price(self):
        return [product.price for product in self.products.all()]


    def total_price(self):
        price = 0
        for p in self.products.all():
            price += p.price

        return price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_addres = models.CharField(max_length=30, default=0)

    def __str__(self):
        return f'{self.user.username} - {self.total_price}'

    @property
    def product_name(self):
        return [product.name for product in self.products.all()]












