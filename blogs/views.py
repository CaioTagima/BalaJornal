from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Task
import json

class TaskView(View):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get("id")
        if task_id:
            task = get_object_or_404(Task, id=task_id)
            return JsonResponse({
                "id": task.id,
                "task_name": task.task_name,
                "task_description": task.task_description,
                "pub_date": task.pub_date,
            })
        else:
            tasks = list(Task.objects.values())
            return JsonResponse(tasks, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            task = Task.objects.create(
                task_name=data.get("task_name", ""),
                task_description=data.get("task_description", ""),
                pub_date=data.get("pub_date", ""),
            )
            return JsonResponse({
                "id": task.id,
                "task_name": task.task_name,
                "task_description": task.task_description,
                "pub_date": task.pub_date,
            }, status=201)
        except Exception:
            return HttpResponseBadRequest("Bad data")

    def put(self, request, *args, **kwargs):
        task_id = kwargs.get("id")
        if not task_id:
            return HttpResponseBadRequest("Missing task ID")
        task = get_object_or_404(Task, id=task_id)
        data = json.loads(request.body)
        task.task_name = data.get("task_name", task.task_name)
        task.task_description = data.get("task_description", task.task_description)
        task.pub_date = data.get("pub_date", task.pub_date)
        task.save()
        return JsonResponse({
            "id": task.id,
            "task_name": task.task_name,
            "task_description": task.task_description,
            "pub_date": task.pub_date,
        })

    def delete(self, request, *args, **kwargs):
        task_id = kwargs.get("id")
        if not task_id:
            return HttpResponseBadRequest("Missing task ID")
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({"message": "Task deleted"})

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'detail': 'CSRF cookie set'})