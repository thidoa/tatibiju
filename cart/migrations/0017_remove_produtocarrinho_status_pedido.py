# Generated by Django 4.0.6 on 2023-01-11 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0016_produtocarrinho_status_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtocarrinho',
            name='status_pedido',
        ),
    ]