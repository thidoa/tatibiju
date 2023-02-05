# Generated by Django 4.0.6 on 2023-01-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_remove_produtocarrinho_status_pedido_carrinho'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtocarrinho',
            name='status_pedido',
            field=models.CharField(blank=True, choices=[('Enviado', 'Enviado'), ('Em andamento', 'Em andamento'), ('Cancelado', 'Cancelado'), ('Finalizado', 'Finalizado')], default='Enviado', max_length=100, null=True),
        ),
    ]
