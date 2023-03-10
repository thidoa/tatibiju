from django.shortcuts import render, redirect, get_object_or_404
from .models import ProdutoCarrinho, Carrinho
from products.models import Product
from users.models import Usuario
from django.contrib import messages
from datetime import datetime

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

        buscar_carrinho = Carrinho.objects.filter(usuario=usuario).filter(status_pedido="Enviado")#.filter(produtos__product=product).filter(produtos__status=True)
        #print(buscar_produto)
        cart = Carrinho.objects.filter(usuario=usuario).filter(status_pedido="Enviado")
        
        # teste = cart.first().produtos.all().filter(product=product).filter(status=True)
        # print(teste)
        if len(buscar_carrinho) == 0:
            carrinho = ProdutoCarrinho.objects.create(product=product, quantidade=quantity)
            carrinho.save()

            cart = Carrinho.objects.create(status_pedido="Enviado")
            cart.save()
            cart.produtos.add(carrinho)
            cart.save()

            usuario.carrinho.add(cart)
            usuario.save()
        else:
            carrinho = buscar_carrinho.first()
            if str(product) in str(carrinho.produtos.all()):
                produtos = carrinho.produtos.filter(product=product)
                produto = produtos.first()
                if produto.status == False:
                    produto.quantidade = int(quantity)
                else:
                    produto.quantidade += int(quantity)
                produto.status = True
                produto.save()
            else:
                produto_carrinho = ProdutoCarrinho.objects.create(product=product, quantidade=quantity)
                produto_carrinho.save()
                carrinho.produtos.add(produto_carrinho)
                carrinho.save()
        

            # primeiro_produto = buscar_produto.first()
            # produto_cadastrado = get_object_or_404(ProdutoCarrinho, id=primeiro_produto.id)
            # produto_cadastrado.quantidade += int(quantity)
            # produto_cadastrado.save()
    cart = Carrinho.objects.filter(usuario=usuario).filter(status_pedido="Enviado")
    calcula_total(request, cart.first().id)

    return redirect('carrinho')





# def add_cart(request, pk):
#     if request.user.is_anonymous:
#         messages.success(request, 'Preciso está logado para adicionar no carrinho!')
#         return redirect('login')
#     usuario_id = request.user.usuario.id
#     usuario = get_object_or_404(Usuario, id=usuario_id)
#     product = get_object_or_404(Product, id=pk)

#     if request.method == "POST":
#         quantity = request.POST['quantity']
#         if int(quantity) < 1:
#             messages.error(request, 'Não é possivel mandar a quantidade 0 de produtos para o carrinho')
#             return redirect('products')

#         buscar_produto = ProdutoCarrinho.objects.filter(usuario=usuario).filter(product=product).filter(status=True)
#         if len(buscar_produto) == 0:
#             carrinho = ProdutoCarrinho.objects.create(product=product, quantidade=quantity)
#             carrinho.save()
#             usuario.produto_carrinho.add(carrinho)
#             usuario.save()
#         else:
#             primeiro_produto = buscar_produto.first()
#             produto_cadastrado = get_object_or_404(ProdutoCarrinho, id=primeiro_produto.id)
#             produto_cadastrado.quantidade += int(quantity)
#             produto_cadastrado.save()

#     return redirect('carrinho')
    

def carrinho(request):
    if request.user.is_anonymous:
        messages.success(request, 'Preciso está logado para adicionar no carrinho!')
        return redirect('login')
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)

    cart = Carrinho.objects.filter(usuario=usuario).filter(status_pedido="Enviado")
    print(usuario.carrinho.all())
    total = 0
    for produto_carrinho in cart:
        for produto in produto_carrinho.produtos.all():
            if produto.status == True:
                total += produto.product.preco * produto.quantidade

    context = {
        'cart': cart,
        'total': total,
    }

    return render(request, 'cart/home.html', context)

def remove_product_cart(request, pk, id_cart):
    # usuario_id = request.user.usuario.id
    # usuario = get_object_or_404(Usuario, id=usuario_id)
    # product = get_object_or_404(Product, id=pk)

    # buscar_carrinho = Carrinho.objects.filter(usuario=usuario).filter(produtos__product=product).filter(produtos__status=True)
    # buscar_produto = buscar_carrinho.first()
    # produtos = buscar_produto.produtos.filter(product=product)

    # primeiro_produto = produtos.first()
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)

    cart = Carrinho.objects.filter(usuario=usuario).filter(status_pedido="Enviado")
    
    primeiro_produto = buscar_primeiro_produto(request, pk)
    
    cart.first().produtos.remove(primeiro_produto)
    
    calcula_total(request, id_cart)
    
    #primeiro_produto.status = False
    #primeiro_produto.save()

    messages.success(request, 'Produto removido do carrinho!')
    return redirect('carrinho')

def update_cart(request, pk, id_cart):
    if request.user.is_anonymous:
        messages.success(request, 'Preciso está logado para adicionar no carrinho!')
        return redirect('login')
    
    if request.method == "POST":
        quantity = request.POST['quantity']
        primeiro_produto = buscar_primeiro_produto(request, pk)

        produto_cadastrado = get_object_or_404(ProdutoCarrinho, id=primeiro_produto.id)
        produto_cadastrado.quantidade = int(quantity)
        produto_cadastrado.save()
        calcula_total(request, id_cart)
        # carrinho = get_object_or_404(Carrinho, produtos=produto_cadastrado)
        # total = 0
        # for produto in carrinho.produtos.all():
        #     total += produto.quantidade * produto.product.preco
        # carrinho.total = total
        # carrinho.save()

    messages.success(request, 'Carrinho atualizado!')
    return redirect('carrinho')


def confirmar_pedido(request):
    user = get_object_or_404(Usuario, id=request.user.usuario.id)
    carrinho = Carrinho.objects.filter(usuario=user).filter(status_pedido="Enviado").filter(produtos__status=True)

    for product in carrinho:
        product.status_pedido = "Em andamento"
        product.save()

    return redirect('pedidos_cliente')

def pedidos_cliente(request):
    user = get_object_or_404(Usuario, id=request.user.usuario.id)
    pedidos = Carrinho.objects.filter(usuario=user).filter(status_pedido="Em andamento")

    if len(pedidos) == 0:
        messages.success(request, 'Não tem pedidos!')
        return redirect('index')

    context = {
        'pedidos': pedidos,
    }

    return render(request, 'users/pedidos_cliente.html', context)

def pedido_cliente(request, pk):
    pedido = get_object_or_404(Carrinho, id=pk)

    tempo = datetime.now()
    print(f'tempo -> {tempo}')

    print(pedido.date_modified.day)

    date_created = pedido.date_created.strftime("%d/%m/%Y %H:%M:%S")
    date_modified = pedido.date_modified.strftime("%d/%m/%Y %H:%M:%S")
    
    print(date_created)
    print(pedido.date_created)

    context = {
        'pedido': pedido,
        'date_created': date_created,
        'date_modified': date_modified,
    }

    return render(request, 'users/pedido_cliente.html', context)


def buscar_primeiro_produto(request, pk):
    usuario_id = request.user.usuario.id
    usuario = get_object_or_404(Usuario, id=usuario_id)
    product = get_object_or_404(Product, id=pk)



    buscar_carrinho = Carrinho.objects.filter(usuario=usuario).filter(produtos__product=product).filter(produtos__status=True)
    buscar_produto = buscar_carrinho.first()
    print(f'buscar_produto - > {buscar_produto}')
    produtos = buscar_produto.produtos.filter(product=product)
    primeiro_produto = produtos.first()

    # buscar_produto = ProdutoCarrinho.objects.filter(usuario=usuario).filter(product=product).filter(status=True)

    # primeiro_produto = buscar_produto.first()
    return primeiro_produto


def calcula_total(request, id_cart):
    carrinho = get_object_or_404(Carrinho, id=id_cart)
    total = 0
    for produto in carrinho.produtos.all():
        total += produto.quantidade * produto.product.preco
    carrinho.total = total
    carrinho.save()


