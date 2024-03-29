from django.urls import path
from .import views

urlpatterns = [
    path('carrinho', views.carrinho, name='carrinho'),
    path('add_cart/<int:pk>', views.add_cart, name='add_cart'),
    path('update_cart/<int:pk>/<int:id_cart>', views.update_cart, name='update_cart'),
    path('remove_product_cart/<int:pk>/<int:id_cart>', views.remove_product_cart, name='remove_product_cart'),
    path('confirmar/pedido', views.confirmar_pedido, name='confirmar_pedido'),
    path('pedidos', views.pedidos_cliente, name='pedidos_cliente'),
    path('pedido_cliente/<int:pk>', views.pedido_cliente, name='pedido_cliente'),
]
