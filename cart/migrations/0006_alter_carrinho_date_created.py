# Generated by Django 4.0.6 on 2023-05-09 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_carrinho_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 9, 15, 58, 32, 174764), null=True),
        ),
    ]