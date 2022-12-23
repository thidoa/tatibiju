from django.db import models

# class Image_product(models.Model):
#     image = models.ImageField(upload_to='joias/')
#     nome = models.CharField(max_length=50)

class Product(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='joias/')
    # image = models.ManyToManyField(Image_product, verbose_name=("Product_image"))

    def __str__(self):
        return self.titulo