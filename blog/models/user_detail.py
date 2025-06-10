from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserDetail(models.Model):  
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='details'
    )
    
    full_name = models.CharField(
        verbose_name='Nome Completo',
        max_length=150,
    )

    address = models.CharField(
        verbose_name='Endereço',
        max_length=150,
    )

    age = models.PositiveIntegerField(  
        verbose_name='Idade',
    )

    cpf = models.CharField(
        verbose_name='CPF',
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message='CPF deve estar no formato 123.456.789-00'
            )
        ]
    )

    def __str__(self):
        return f"Detalhes de {self.user.username}"
