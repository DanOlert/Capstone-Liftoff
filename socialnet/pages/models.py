from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default='default.png', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    featured = models.CharField(max_length=500, null=True, blank=True, default=None)

    # def _get_help_text(self, field_name):
    #     for field in self._meta.fields:
    #         if field.name == field_name:
    #             return field.help_text

    def __str__(self):
        return self.title
