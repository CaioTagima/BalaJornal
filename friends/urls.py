from django.urls import path
from friends import views

urlpatterns = [
    path('send/<int:id_sender>/<int:id_receiver>/', views.send_request, name='send_request'),
    path('accept/<int:id_sender>/<int:id_receiver>/', views.accept_request, name='accept_request'),
    path('reject/<int:id_sender>/<int:id_receiver>/', views.reject_request, name='reject_request'),
    path('remove/<int:id_sender>/<int:id_receiver>/', views.remove_friend, name='remove_friend'),
    path('list/<int:id_user>/', views.list_friends, name='list_friends'),
]
