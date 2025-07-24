from django.shortcuts import render, redirect
from users.forms import LoginForms, RegisterForms
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

User = get_user_model()

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form['email'].value()
            senha = form['senha'].value()

            usuario = authenticate(
                request,
                username=email,
                password=senha,
            )

            if usuario is not None:
                auth_login(request, usuario)
                messages.success(request, f"Você logado com sucesso!!")
                return redirect('index')
            else:
                messages.error(request, "Erro ao efetuar Login")
                return redirect('login')

    return render(request, "users/login.html", {'form': form})

def register(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, "Erro na confirmação de Senha")
                return redirect('register')

            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(email=email).exists():
                messages.error(request, "Usuário já existente")
                return redirect('register')

            usuario = User.objects.create_user(
                email=email,
                password=senha,
            )
            usuario.save()

            messages.success(request, "Cadastro efetuado com Sucesso")
            return redirect('login')

    return render(request, "users/register.html", {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')
