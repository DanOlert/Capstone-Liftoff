from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    #TODO make slug feild automatically generate slug
    slug = models.SlugField(unique=True)
    body = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    #if we use a thumbnail, use: thumb = models.ImageField(defaul='default.png', blank=True) may not use this.


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:111]
