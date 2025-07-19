from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
