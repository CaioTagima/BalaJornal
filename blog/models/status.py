from django.db import models


class Status(models.TextChoices):
    CREATED = 'C', 'Criado'
    ON_GOING = 'E', 'Em andamento'
    FINISHED = 'F', 'Finalizado'
    NULL = '', '-----'
