from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User 
from django.contrib import auth, messages
from .models import Usuario
from cart.models import ProdutoCarrinho, Carrinho
from .forms import UserUpdateForm

def cadastro(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        tipo = request.POST['tipo']
        telefone = request.POST['telefone']
        senha = request.POST['password']
        verificacao_senha = request.POST['verification_password']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco!')
            return redirect('cadastro')
        if senha != verificacao_senha:
            messages.error(request, 'As senhas não são iguais!')
            return redirect('cadastro')
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado!')
            return redirect('login')
        
        user = Usuario.objects.create_user(username=nome, email=email, password=senha, tipo=tipo, telefone=telefone)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'users/cadastro.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['password']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if Usuario.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password = senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha incorretos!')
        else:
            messages.error(request, 'Usuário inexistente ou campos incorretos!')
    return render(request, 'users/login.html')

def update_user(request):
    if request.user.is_anonymous:
        return redirect('index')
    
    user = get_object_or_404(Usuario, id=request.user.id)
    
    form = UserUpdateForm(dict(
        username=user.username,
        email=user.email,
        telefone=user.telefone,
    ))

    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.update_form(user.id)
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'users/update_user.html', context)


def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('login')

def campo_vazio(campo):
    return not campo.strip()

def pedidos(request):
    users = Usuario.objects.exclude(carrinho=None).exclude(carrinho__status_pedido="Enviado").distinct()
    total = 0
    for user in users:
        for carrinho in user.carrinho.all():
            for produto in carrinho.produtos.all():
                total +=  produto.product.preco

    context = {
        'usuarios': users,
    }

    return render(request, 'users/pedidos_gerente.html', context)

def mudarStatusPedido(request, id):
    carrinho = get_object_or_404(Carrinho, id=id)

    if request.method == "POST":
        status = request.POST['statusPedido']
        
        carrinho.status_pedido = status
        carrinho.save()

    return redirect('pedidos')

def cancelamento(request, id):
    pedido = get_object_or_404(Carrinho, id=id)
    
    if request.method == "POST":
        motivo_cancelamento = request.POST['cancelamento']

        pedido.motivo_cancelamento = motivo_cancelamento
        pedido.status_pedido = "Cancelado"
        pedido.save()
        messages.success(request, 'Pedido cancelado com sucesso!')
        return redirect('index')

    context = {
        'pedido': pedido,
    }
    return render(request, 'users/cancelamento.html', context)

def buscar(request):
    if 'buscar' in request.GET:
        id_a_buscar = request.GET['buscar']
        if id_a_buscar == '':
            return redirect('pedidos')
        elif buscar:
            pedido = Carrinho.objects.filter(id=id_a_buscar)
            usuario = Usuario.objects.filter(carrinho__id=id_a_buscar)

            # teste_pedido = Carrinho.objects.filter(status_pedido="Em andamento")
            # teste = Usuario.objects.filter(carrinho__status_pedido="Em andamento")

        
            # print(teste)


    context = {
        'usuario': usuario,
        'pedidos': pedido,
    }
    return render(request, 'buscar.html', context)
