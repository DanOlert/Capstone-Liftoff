from django import forms
from django.utils.text import slugify

from . import models

class EditPage(forms.ModelForm):
    class Meta:
        model = models.Page
        fields = [
            'title',
            'description',
            'photo',
            'featured',
            ]
