# Generated by Django 4.0.6 on 2023-05-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reservados',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
