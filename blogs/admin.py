from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_name", "status", "pub_date")
    list_filter = ("status",)
