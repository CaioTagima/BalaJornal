from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    email = models.EmailField(
        primary_key=True,
        unique=True,
        verbose_name='E-mail',
        blank=False,  
        null=False,   
        error_messages={
            'unique': 'Este e-mail já está cadastrado.',
            'blank': 'O e-mail é obrigatório.',
            'null': 'O e-mail é obrigatório.'
        }
    )

    username = models.CharField(
        verbose_name='Nome de Usuário',
        blank=False,
        null=False,
        error_messages={
            'blank': 'O nome de usuário é obrigatório.',
            'null': 'O nome de usuário é obrigatório.'
        }
    )
    
    USERNAME_FIELD = 'email'      
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

