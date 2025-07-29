from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class FriendRequest(models.Model):
    STATUS_CHOICES = [
        ("P", "Pendente"),
        ("A", "Aceito"),
        ("R", "Recusado"),
    ]

    sent = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="Solicitaçoes enviadas")
    recived = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="Solicitaçoes recebidas")
    status = models.CharField(max_length=1, choices = STATUS_CHOICES, default="P")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sent} -> {self.recived} ({self.status})"
