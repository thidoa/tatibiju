from django.urls import path

from .views import index, product_list_view, product_list_detail, form_modelform
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('products/', product_list_view),
    path('products/<int:pk>', product_list_detail, name="product_detail"),
    path('modelform/', form_modelform, name="form_modelform")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
