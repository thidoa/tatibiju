from django.db import models
from django.contrib.auth.models import User
from cart.models import Carrinho

class Usuario(User):

    cargos = (
        ('Cliente', 'Cliente'),
        ('Gerente', 'Gerente'),
    )
    tipo = models.CharField(max_length=100, default="Cliente",choices=cargos)
    carrinho = models.ManyToManyField(Carrinho, blank=True, null=True)

    def __str__(self):
        return self.username