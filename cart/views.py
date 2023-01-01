from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrinho
from products.models import Product
from users.models import Usuario
from django.contrib import messages

def add_cart(request, pk):
    if request.user.is_anonymous:
        messages.success(request, 'Preciso está logado para adicionar no carrinho!')
        return redirect('login')
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        quantity = request.POST['quantity']
        if int(quantity) < 1:
            messages.error(request, 'Não é possivel mandar a quantidade 0 de produtos para o carrinho')
            return redirect('products')

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

def update_cart(request, pk):
    if request.user.is_anonymous:
        messages.success(request, 'Preciso está logado para adicionar no carrinho!')
        return redirect('login')
    
    if request.method == "POST":
        quantity = request.POST['quantity']
        primeiro_produto = buscar_primeiro_produto(request, pk)

        produto_cadastrado = get_object_or_404(Carrinho, id=primeiro_produto.id)
        produto_cadastrado.quantidade = int(quantity)
        produto_cadastrado.save()

    messages.success(request, 'Carrinho atualizado!')
    return redirect('carrinho')

def buscar_primeiro_produto(request, pk):
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)
    product = get_object_or_404(Product, id=pk)

    buscar_produto = Carrinho.objects.filter(usuario=usuario).filter(product=product).filter(status=True)

    primeiro_produto = buscar_produto.first()
    return primeiro_produto