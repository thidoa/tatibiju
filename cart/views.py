from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Carrinho
from products.models import Product
from users.models import Usuario
from django.contrib import messages

def home(request):
    if request.user.is_anonymous:
        return redirect('index')
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "cart/home.html")

def update(request):
    product_id = 9
    # Pega o produto com id 1
    product_obj = Product.objects.get(id=product_id)
    # Cria ou pega a instancia já existente do carrinho
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # E o produto se adiciona a instancia do campo M2M
    cart_obj.products.add(product_obj) 
    # cart_obj.product.remove(product_obj)
    return redirect('home')

def add_cart(request, pk):
    if request.user.is_anonymous:
        messages.success(request, 'Preciso está logado para adicionar no carrinho!')
        return redirect('login')
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        quantity = request.POST['quantity']
        buscar_produto = Carrinho.objects.filter(usuario=usuario).filter(product=product).filter(status=True)
        if len(buscar_produto) == 0:
            carrinho = Carrinho.objects.create(product=product, usuario=usuario, quantidade=quantity)
            carrinho.save()
        else:
            primeiro_produto = buscar_produto.first()
            produto_cadastrado = get_object_or_404(Carrinho, id=primeiro_produto.id)
            produto_cadastrado.quantidade += int(quantity)
            produto_cadastrado.save()

    return redirect('carrinho')
    

def carrinho(request):
    if request.user.is_anonymous:
        messages.success(request, 'Preciso está logado para adicionar no carrinho!')
        return redirect('login')
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)

    cart = Carrinho.objects.filter(usuario=usuario)
    total = 0
    for produto in cart:
        if produto.status == True:
            total += produto.product.preco * produto.quantidade

    context = {
        'cart': cart,
        'total': total,
    }

    return render(request, 'cart/home.html', context)

def remove_product_cart(request, pk):
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)
    product = get_object_or_404(Product, id=pk)

    buscar_produto = Carrinho.objects.filter(usuario=usuario).filter(product=product).filter(status=True)
    primeiro_produto = buscar_produto.first()

    primeiro_produto.status = False
    primeiro_produto.save()

    messages.success(request, 'Produto removido do carrinho!')
    return redirect('carrinho')
