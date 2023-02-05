# Generated by Django 4.0.6 on 2023-01-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_remove_produtocarrinho_status_pedido'),
        ('users', '0006_remove_usuario_carrinho_usuario_produto_carrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='produto_carrinho',
        ),
        migrations.AddField(
            model_name='usuario',
            name='carrinho',
            field=models.ManyToManyField(blank=True, null=True, to='cart.carrinho'),
        ),
    ]
