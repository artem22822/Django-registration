from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])

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










    #created_at = models.DateTimeField(default=timezone.now)
    #updated_at = models.DateTimeField(auto_now=True)
    #total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0, )
    #product_list = Product.objects.get(id=1)






