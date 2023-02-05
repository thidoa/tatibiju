# Generated by Django 4.0.6 on 2023-01-08 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cart', '0009_alter_produtocarrinho_status_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtocarrinho',
            name='status',
        ),
        migrations.RemoveField(
            model_name='produtocarrinho',
            name='status_pedido',
        ),
        migrations.RemoveField(
            model_name='produtocarrinho',
            name='usuario',
        ),
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('status_pedido', models.CharField(blank=True, choices=[('Enviado', 'Enviado'), ('Em andamento', 'Em andamento'), ('Cancelado', 'Cancelado'), ('Finalizado', 'Finalizado')], default='Enviado', max_length=100, null=True)),
                ('produtos_carrinho', models.ManyToManyField(to='cart.produtocarrinho')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usuario')),
            ],
        ),
    ]
