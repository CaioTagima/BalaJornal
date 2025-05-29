from django.http import HttpResponse
from django.template import loader
from blog.models.task import Task
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_add_task = Task.objects.order_by("-created_at")[:5]
    template = loader.get_template('blog/index.html')
    context = {"latest_add_task": latest_add_task}
    return HttpResponse(template.render(context, request))

def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "blog/task.html", {"task": task})
