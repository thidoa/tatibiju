from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProdutoForm
from django.contrib.auth.models import User
from users.models import Usuario
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def product_list(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'list.html', context)

def product_detail(request, pk):
    instance = get_object_or_404(Product, pk = pk)
    # img = Image_product.objects.all()
    # image = instance.image.all
    # print(dir(request.session))
    context = {
        'object': instance,
    }
    return render(request, 'detail.html', context)

def create_product(request):
    form = ProdutoForm()
    if request.user.is_anonymous:
        return redirect('index')
    if request.user.usuario.tipo == "Cliente":
        return redirect('index')
    
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save() 
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('products')   
    
    context = {
        'form': form
    }
    
    return render(request, "product_modelform.html", context)

def update(request, pk):
    if request.user.is_anonymous:
        return redirect('index')
    if request.user.usuario.tipo == "Cliente":
        return redirect('index')

    product = Product.objects.get(id=pk)
    form = ProdutoForm(instance=product)

    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'product_modelform.html', context)

def delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    products = Product.objects.all()

    context = {
        'object_list': products
    }

    return render(request, 'list.html', context)