from django.contrib import admin
from .models import Product

# Register your models here.
# admin.site.register(Image_product)


@admin.register(Product)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'categoria', 'preco', 'estoque', 'reservados', 'date')
    list_filter = ('categoria', )