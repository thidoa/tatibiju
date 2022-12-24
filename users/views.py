from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import auth, messages
from .models import Usuario

def cadastro(request):
    if request.method == "POST":
        nome = request.POST['nome']
        email = request.POST['email']
        tipo = request.POST['tipo']
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
        user = Usuario.objects.create_user(username=nome, email=email, password=senha, tipo=tipo)
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
    return render(request, 'users/login.html')


def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')


def campo_vazio(campo):
    return not campo.strip()