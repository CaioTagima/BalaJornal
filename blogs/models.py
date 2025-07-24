from django.db import models
from datetime import datetime, timedelta


class Task(models.Model):
    STATUS_CHOICES = [
        ("P", "Pendente"),
        ("A", "Em andamento"),
        ("C", "Concluída"),
    ]

    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")
    expiration_date = models.DateTimeField("expiration date", default= datetime.now()+timedelta(days=1))

