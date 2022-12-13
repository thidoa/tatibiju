from django.db import models

class Product(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='joias/')

    def __str__(self):
        return self.titulo