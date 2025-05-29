from django.db import models
from .priority import Priority
from .status import Status
from .type import Type


class Task(models.Model):
    title = models.TextField(verbose_name='Título')
    description = models.TextField(blank=True, default='', verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Horário de Criação')
    pub_expiration_date = models.DateTimeField(null=True, blank=True, verbose_name='Prazo da Tarefa')
    priority = models.CharField(blank=True, max_length=1, default=Priority.NULL, choices=Priority.choices, verbose_name='Prioridade')
    type = models.CharField(blank=True, max_length=1, default=Type.NULL, choices=Type.choices, verbose_name='Tipo da Tarefa')
    status = models.CharField(blank=True, max_length=1, default=Status.NULL, choices=Status.choices, verbose_name='Status')

    def __str__(self):
        return self.title
