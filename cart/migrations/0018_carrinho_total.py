# Generated by Django 4.0.6 on 2023-01-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_remove_produtocarrinho_status_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True),
        ),
    ]