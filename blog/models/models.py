from django.db import models


class Task(models.Model):

    status = [
        ('C', 'Criado'),
        ('E', 'Em andamento'),
        ('F', 'Finalizado'),
    ]

    type = [
        ('L', 'Lembrete'),
        ('E', 'Evento'),
        ('N', 'Nota'),
        ('M', 'Meta'),
    ]

    priority = [ 
        ('A', 'Alta'),
        ('M', 'Média'),
        ('B', 'Baixa')
    ]

    title = models.CharField(max_length=50, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Horário de Criação')
    pub_expiration_date = models.DateTimeField(verbose_name='Prazo da Tarefa')
    priority = models.CharField(max_length=1, default='M', choices=priority,verbose_name='Prioridade')
    type = models.CharField(max_length=1, default='L', choices=type,verbose_name='Tipo da Tarefa')
    status = models.CharField(max_length=1, default='C', choices=status,verbose_name='Status')
        
    def __str__(self):
        return self.title



