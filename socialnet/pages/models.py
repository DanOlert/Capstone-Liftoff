from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    listening = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default='default.png', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.title
