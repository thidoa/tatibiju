# Generated by Django 4.0.6 on 2023-02-05 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0029_alter_carrinho_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 5, 17, 8, 28, 606991, tzinfo=utc), null=True),
        ),
    ]
