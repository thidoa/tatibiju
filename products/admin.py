from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'preco')