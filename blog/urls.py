from django.urls import path

from BalaJornal.blog.views import blog_view

app_name = "blog"
urlpatterns = [
    path("", blog_view.index, name="index"),
    path("task/<int:task_id>/", blog_view.task, name="task"),
]
