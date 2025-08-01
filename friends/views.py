from .models import Friend
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_request(request, id_sender, id_receiver):

    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    sender = get_object_or_404(CustomUser, id = id_sender)
    receiver = get_object_or_404(CustomUser, id = id_receiver)

    Friend.objects.create(
        id_sender=sender,
        id_receiver=receiver,
        status_id_sender = "A",
        status_id_receiver = "P",
        is_friend=False,
    )

    return JsonResponse({'message': 'Solicitação enviada com sucesso.'}, status=201)

@csrf_exempt
def accept_request(request, id_sender, id_receiver):
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
    sender = get_object_or_404(CustomUser, id=id_sender)
    receiver = get_object_or_404(CustomUser, id=id_receiver)
    friendship = Friend.objects.filter(id_sender=sender, id_receiver=receiver).first()

    if not friendship:
        return JsonResponse({'error': 'Solicitação não encontrada'}, status=404)

    friendship.status_id_receiver = "A"
    friendship.status_id_sender = "A"
    friendship.is_friend = True
    friendship.save()

    return JsonResponse({'message': 'Solicitação aceita com sucesso.'}, status=200)

@csrf_exempt
def reject_request(request, id_sender, id_receiver):
    
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
    sender = get_object_or_404(CustomUser, id=id_sender)
    receiver = get_object_or_404(CustomUser, id=id_receiver)
    friendship = Friend.objects.filter(id_sender=sender, id_receiver=receiver).first()

    if not friendship:
        return JsonResponse({'error': 'Solicitação não encontrada'}, status=404)

    friendship.status_id_receiver = "R"
    friendship.status_id_sender = "A"
    friendship.is_friend = False
    friendship.save()
    
    return JsonResponse({'message': 'Solicitação rejeitada com sucesso.'}, status=200)

@csrf_exempt
def remove_friend(request, id_sender, id_receiver):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    sender = get_object_or_404(CustomUser, id=id_sender)
    receiver = get_object_or_404(CustomUser, id=id_receiver)

    friendship = Friend.objects.filter(id_sender=sender, id_receiver=receiver, is_friend=True).first()

    if not friendship:
        friendship = Friend.objects.filter(id_sender=receiver, id_receiver=sender, is_friend=True).first()

    if not friendship:
        return JsonResponse({'error': 'Amizade não encontrada.'}, status=404)

    friendship.delete()

    return JsonResponse({'message': 'Amizade removida com sucesso.'}, status=200)

@csrf_exempt
def list_friends(request, id_user):

    if request.method != 'GET':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    user = get_object_or_404(CustomUser, id=id_user)
    sent = Friend.objects.filter(id_sender=user, is_friend=True)
    received = Friend.objects.filter(id_receiver=user, is_friend=True)

    friends = []
    for f in sent:
        friends.append({'email': f.id_receiver.email})
    for f in received:
        friends.append({'email': f.id_sender.email})

    return JsonResponse({'friends': friends}, status=200)
    
