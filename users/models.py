from django.db import models
from django.contrib.auth.models import User

class Usuario(User):

    cargos = (
        ('Cliente', 'Cliente'),
        ('Gerente', 'Gerente'),
    )
    tipo = models.CharField(max_length=100, default="Cliente",choices=cargos)

    def __str__(self):
        return self.username