from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

#class User(AbstractUser): 
#    username = models.CharField(max_length=255, unique=True)
#    first_name = models.CharField(max_length=255)
#    last_name = models.CharField(max_length=255)
#    email = models.EmailField(max_length=255, unique=True)

User = get_user_model()



class EmailOTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.otp}"
    
    def is_expired(self):
        return timezone.now() > self.created_at + timedelta(minutes=10)

# Create your models here.
class ChatMessage(models.Model):
    room_id = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_id} | {self.user}: {self.message}"