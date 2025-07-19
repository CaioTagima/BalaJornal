from django.urls import path

from .views import TaskView, get_csrf_token

urlpatterns = [
    path('tasks', TaskView.as_view(), name='book-list-create'),
    path('tasks/<int:id>/', TaskView.as_view(), name='book-detail'),
    path('get-csrf-token', get_csrf_token, name='get_csrf_token'),
]