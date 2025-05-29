from django.db import models


class Type(models.TextChoices):
    REMINDER = 'L', 'Lembrete'
    EVENT = 'E', 'Evento'
    NOTE = 'N', 'Nota'
    GOAL = 'M', 'Meta'
    NULL = '', '-----'
