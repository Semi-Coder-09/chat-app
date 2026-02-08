from django.db import models

# Create your models here.
class User_data(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    
class Chat(models.Model):
    sender = models.ForeignKey(
        User_data,
        related_name='sent_messages',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User_data,
        related_name='received_messages',
        on_delete=models.CASCADE
    )
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class BlockedUser(models.Model):
    blocker = models.ForeignKey(
        User_data,
        related_name='blocked_users',
        on_delete=models.CASCADE
    )
    blocked = models.ForeignKey(
        User_data,
        related_name='blocked_by',
        on_delete=models.CASCADE
    )
    blocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('blocker', 'blocked')

    def __str__(self):
        return f"{self.blocker} blocked {self.blocked}"
    