from django.db import models


class Priority(models.TextChoices):
    HIGH = 'A', 'Alta'
    MEDIUM = 'M', 'Média'
    LOW = 'B', 'Baixa'
    NULL = '', '-----'
