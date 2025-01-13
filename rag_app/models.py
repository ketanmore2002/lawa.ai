from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

 
class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True,)
    title = models.CharField(max_length=255,null=True,blank=True)
    share_id = models.CharField(max_length=255, unique=True,null=True,blank=True)
    user = models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE,null=True,blank=True)
 
    # def __str__(self):
    #     return f"Chat(id={self.id}, title={self.title}, user_id={self.user.id})"
 
 
class Interaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_message = models.TextField(null=True,blank=True)
    llm_response = models.TextField(null=True,blank=True)
    chat = models.ForeignKey(Chat, related_name='interactions', on_delete=models.CASCADE,null=True,blank=True)
    timestamp = models.DateTimeField(default=timezone.now, editable=False,null=True,blank=True)
 
    def __str__(self):
        return f"Interaction(id={self.id}, chat_id={self.chat.id}, timestamp={self.timestamp})"
 
 
class LoginHistory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User,related_name='login_history', on_delete=models.CASCADE,null=True,blank=True)
    login_at = models.DateTimeField(default=timezone.now, editable=False,null=True,blank=True)
    ip_address = models.GenericIPAddressField(null=True,blank=True)
    user_agent = models.CharField(max_length=255,null=True,blank=True)
 
    def __str__(self):
        return f"LoginHistory(id={self.id}, user_id={self.user.id}, login_at={self.login_at})"
 
 
# class UserAnalytics(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     user = models.ForeignKey(User, related_name='analytics', on_delete=models.CASCADE)
#     date = models.DateField(default=timezone.now)
#     total_messages = models.IntegerField(default=0)
#     total_chats = models.IntegerField(default=0)
#     avg_messages_per_chat = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
#     last_updated = models.DateTimeField(auto_now=True)
 
#     class Meta:
#         unique_together = ('user', 'date')
#         verbose_name = "User Analytics"
#         verbose_name_plural = "User Analytics"
 
#     def __str__(self):
#         return f"UserAnalytics(id={self.id}, user_id={self.user.id}, date={self.date})"