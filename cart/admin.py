from django.contrib import admin
from .models import ProdutoCarrinho, Carrinho

# admin.site.register(ProdutoCarrinho)
@admin.register(ProdutoCarrinho)
class ProdutoCarrinhoAdmin(admin.ModelAdmin): 
    list_display = ('id', 'product', 'quantidade')

# admin.site.register(Carrinho)
@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'status_pedido', 'motivo_cancelamento')
    list_filter = ('status_pedido',)