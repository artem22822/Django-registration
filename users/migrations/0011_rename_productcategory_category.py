# Generated by Django 4.1.6 on 2023-02-24 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='Category',
        ),
    ]
