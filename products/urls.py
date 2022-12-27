from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('create/product/', views.create_product, name="create_product"),
    path('products/', views.product_list, name='products'),
    path('products/<int:pk>', views.product_detail, name="product_detail"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
