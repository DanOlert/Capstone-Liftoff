from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserSettings(models.Model):
    title = models.CharField(max_length=100, default="User's Settings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
