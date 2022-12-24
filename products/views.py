from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProdutoForm
from django.contrib.auth.models import User
from users.models import Usuario
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
    # img = Image_product.objects.all()
    # image = instance.image.all
    # print(dir(request.session))
    context = {
        'object': instance,
    }
    return render(request, 'detail.html', context)

def form_modelform(request):
    form = ProdutoForm()
    if request.user.is_anonymous:
        return redirect('index')
    if request.user.usuario.tipo == "Cliente":
        return redirect('index')
    
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save()    
    
    context = {
        'form': form
    }
    
    return render(request, "product_modelform.html", context)