from django.urls import path
from .import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('carrinho', views.carrinho, name='carrinho'),
    path('update', views.update, name='update'),
    path('add_cart/<int:pk>', views.add_cart, name='add_cart'),
    path('remove_product_cart/<int:pk>', views.remove_product_cart, name='remove_product_cart'),
]
