from django.db import models
from users.models import CustomUser 

class Friend(models.Model):

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Accepted'),
        ('R', 'Rejected'),
    ]

    id_sender = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    id_receiver = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)

    status_id_sender = models.CharField(choices=STATUS_CHOICES, max_length=20, blank=True, null=True)
    status_id_receiver = models.CharField(choices=STATUS_CHOICES ,max_length=20, blank=True, null=True)
    is_friend = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_sender} -> {self.id_receiver} | Amigo: {self.is_friend}"
