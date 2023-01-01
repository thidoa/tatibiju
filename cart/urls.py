from django.urls import path
from .import views

urlpatterns = [
    path('carrinho', views.carrinho, name='carrinho'),
    path('add_cart/<int:pk>', views.add_cart, name='add_cart'),
    path('update_cart/<int:pk>', views.update_cart, name='update_cart'),
    path('remove_product_cart/<int:pk>', views.remove_product_cart, name='remove_product_cart'),
]
