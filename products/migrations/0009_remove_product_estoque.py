# Generated by Django 4.0.6 on 2022-12-24 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_estoque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='estoque',
        ),
    ]
