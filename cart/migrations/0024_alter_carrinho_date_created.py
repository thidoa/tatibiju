# Generated by Django 4.0.6 on 2023-01-29 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_alter_carrinho_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 29, 15, 23, 51, 783340, tzinfo=utc), null=True),
        ),
    ]