# produtos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Produto
from .forms import ProdutoForm

# Função para verificar se o usuário é administrador (superusuário)
def admin_check(user):
    return user.is_superuser  # Verifica se o usuário é um superusuário (admin)

# Lista de produtos (disponível para todos os usuários)
def listar_produtos(request):
    produtos = Produto.objects.all()  # Todos os produtos
    return render(request, 'produtos/listar.html', {'produtos': produtos})

# Adicionar produto (somente administradores podem adicionar produtos)
@login_required  # Garante que o usuário esteja logado
@user_passes_test(admin_check)  # Garante que o usuário seja um administrador
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produtos:listar_produtos')  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar.html', {'form': form})

# Editar produto (somente administradores podem editar)
@login_required  # Garante que o usuário esteja logado
@user_passes_test(admin_check)  # Garante que o usuário seja um administrador
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar.html', {'form': form, 'produto': produto})

# Remover produto (somente administradores podem remover)
@login_required  # Garante que o usuário esteja logado
@user_passes_test(admin_check)  # Garante que o usuário seja um administrador
def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('produtos:listar_produtos')

# Cadastro de usuário
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Cria o usuário
            login(request, user)  # Faz o login automático do usuário recém-criado
            return redirect('listar_produtos')  # Redireciona para a página principal (produtos)
    else:
        form = UserCreationForm()  # Formulário vazio

    return render(request, 'produtos/cadastro.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.all()  # Todos os produtos
    print(produtos)  # Isso imprimirá os produtos no terminal
    return render(request, 'produtos/listar.html', {'produtos': produtos})


