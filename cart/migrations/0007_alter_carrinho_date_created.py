# Generated by Django 4.0.6 on 2023-05-09 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_carrinho_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 9, 16, 2, 51, 947663), null=True),
        ),
    ]