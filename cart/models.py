from django.db import models
from products.models import Product
from users.models import Usuario

User = Usuario

class Carrinho(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  quantidade = models.IntegerField(default=0)
  status = models.BooleanField(default=True)