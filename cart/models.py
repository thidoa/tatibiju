from django.db import models
from products.models import Product
from datetime import datetime
from pytz import timezone

# from users.models import Usuario

# User = Usuario

class ProdutoCarrinho (models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  # usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  quantidade = models.IntegerField(default=0)
  status = models.BooleanField(default=True)

  # pedido = (
  #   ('Enviado', 'Enviado'),
  #   ('Em andamento', 'Em andamento'),
  #   ('Cancelado', 'Cancelado'),
  #   ('Finalizado', 'Finalizado')
  # )
  # status_pedido = models.CharField(choices=pedido, default="Enviado", max_length=100, blank=True, null=True)

  def __str__(self):
    return self.product.titulo


def dataa():
  tempo = datetime.now(timezone('America/Sao_Paulo'))
  print(f'agora vai-------> {tempo}')
  return tempo

class Carrinho(models.Model):
  produtos = models.ManyToManyField(ProdutoCarrinho, blank=True, null=True)

  total = models.DecimalField(max_digits=100, decimal_places=2, default=0, blank=True, null=True)
  
  date_created = models.DateTimeField(default=dataa(), blank=True, null=True)
  date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)


  pedido = (
    ('Enviado', 'Enviado'),
    ('Em andamento', 'Em andamento'),
    ('Cancelado', 'Cancelado'),
    ('Finalizado', 'Finalizado')
  )
  status_pedido = models.CharField(choices=pedido, default="Enviado", max_length=100, blank=True, null=True)

