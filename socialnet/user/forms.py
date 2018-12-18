from django import forms

from . import models

class EditStats(forms.ModelForm):
    class Meta:
        model = models.UserStats
        fields = [
            'role',
            'availability',
            'genre',
            'location',
            'lookingfor',
            'seriousness',
            ]
