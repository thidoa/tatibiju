from django.urls import path
from .import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index'),
    path('pedidos', views.pedidos, name='pedidos'),
    path('buscar', views.buscar, name='buscar'),
    path('mudarStatusPedido/<int:id>', views.mudarStatusPedido, name='mudarStatusPedido')
]
