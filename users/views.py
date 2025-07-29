from django.shortcuts import render, redirect, get_object_or_404
from users.forms import LoginForms, RegisterForms
from django.contrib.auth import get_user_model, authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import FriendRequest
from django.db.models import Q
from django.views import View

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

class AddFriend(View):
    def send_request(request, send_id):
        send = get_object_or_404(User, id=send_id)
    
        FriendRequest, created = FriendRequest.objects.get_or_create(
        recived=request.user,
        send=send
        )

        if not created:
            messages.error(request, "Solicitação já enviada")
            return redirect('send_request', send_id=send_id)

        messages.success(request, "Solicitação enviada com sucesso")
        return redirect('list_friends')

    def accept_request(request, recived_id):
        FriendRequest = get_object_or_404(
            FriendRequest,
            recived_id=recived_id,#id do usuario que recebeu
            send=request.user,#id do usuario que enviou 
            status='pending'
        )
        FriendRequest.status = 'accepted'
        FriendRequest.save()
        messages.success(request, "Solicitação enviada com sucesso")
        return redirect('list_friends')

    def remove_friend(request, friend_id):
        try:
            FriendRequest = FriendRequest.objects.get(
                Q(recived=request.user, send_id=friend_id) |
                Q(recived_id=friend_id, send=request.user),
                status='accepted'
            )
            FriendRequest.delete()
            messages.success(request, "Amizade removida")
            return redirect('list_friends')
        except FriendRequest.DoesNotExist:
            messages.error(request, "Amizade nao encontrada")
            return redirect('list_friends')
    
    def list_friends(request):
        friend_list = FriendRequest.objects.filter(
            send=request.user,
            status='accepted'
        )
        friends = [f.send.username for f in friend_list]

        if not friends:
            messages.info(request, "Você ainda não tem amigos adicionados.")

        else:
            friends_str = ', '.join(friends)
            messages.success(request, f"Seus amigos: {friends_str}")

        return redirect('list_friends')