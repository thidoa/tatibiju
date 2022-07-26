from django.urls import path

from .views import index, product_list_view, product_list_detail

urlpatterns = [
    path('', index),
    path('products/', product_list_view),
    path('products/<int:pk>', product_list_detail),
]