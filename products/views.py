from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'list.html', context)

def product_list_detail(request, pk):
    instance = get_object_or_404(Product, pk = pk)

    context = {
        'object': instance
    }
    return render(request, 'detail.html', context)