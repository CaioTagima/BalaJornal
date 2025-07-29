from django.urls import path
from users.views import login, register, logout, AddFriend

add_friend = AddFriend()

urlpatterns = [
    #auth
    path('login', login, name='login'),
    path('register',register, name='register'),
    path('logout', logout, name='logout'),
    #friend
    path('friend/send/<int:send_id>/', add_friend.send_request, name='send_request'),
    path('friend/accept/<int:recived_id>/', add_friend.accept_request, name='accept_request'),
    path('friend/remove/<int:friend_id>/', add_friend.remove_friend, name='remove_friend'),
    path('friend/list/', add_friend.list_friends, name='list_friends'),
]