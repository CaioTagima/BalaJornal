from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Task
from django.db.models import Q
from datetime import datetime, timedelta
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
                "expiration_date": task.expiration_date,
                "status": task.status,
            })
        else:
            tasks = Task.objects.all()
            keyword = request.GET.get("keyword")
            #keyword
            if keyword:
                tasks = tasks.filter(
                Q(task_name__icontains=keyword) | Q(task_description__icontains=keyword)
        )
            #status
            status = request.GET.get("status")
            if status:
                tasks = tasks.filter(status=status)
            
            #data
            pub_date = request.GET.get("pub_date")
            if pub_date:
                tasks = tasks.filter(pub_date__date=pub_date)

            #expired
            data_enviada = request.GET.get("expired")
            if data_enviada:
                tasks = tasks.filter(expiration_date__lt = data_enviada)

            #notexpired
            data_enviada = request.GET.get("not expired")
            if data_enviada:
                tasks = tasks.filter(expiration_date__gt = data_enviada)

            #today
            data_enviada = request.GET.get("today")
            if data_enviada:
                tasks = tasks.filter(expiration_date__date = data_enviada)         

            return JsonResponse(list(tasks.values()), safe=False)


    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            task = Task.objects.create(
                task_name=data.get("task_name", ""),
                task_description=data.get("task_description", ""),
                pub_date=data.get("pub_date", ""),
                expiration_date=data.get("expiration_date", ""),
                status=data.get("status", "P"),
            )
            return JsonResponse({
                "id": task.id,
                "task_name": task.task_name,
                "task_description": task.task_description,
                "pub_date": task.pub_date,
                "expiration_date": task.expiration_date,
                "status": task.status,
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
        task.expiration_date = data.get("expiration_date", task.expiration_date)
        task.status = data.get("status", task.status)
        task.save()
        return JsonResponse({
            "id": task.id,
            "task_name": task.task_name,
            "task_description": task.task_description,
            "pub_date": task.pub_date,
            "expiration_date": task.expiration_date,
            "status": task.status,
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