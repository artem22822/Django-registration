# Generated by Django 4.1.6 on 2023-02-23 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_order_delivery_addres'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
