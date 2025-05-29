from django.urls import path

from blog.views import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("task/<int:task_id>/", views.task, name="task"),
]
