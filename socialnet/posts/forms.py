from django import forms
from django.utils.text import slugify

from . import models

#TODO this is how to make a form based on a model
class NewPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'title',
            'type',
            'body',
            'musicembed',
            'type',
            'privacy',
            ]

    # def save(self):
    #     user = request.user
    #     instance = super(AddForm, self).save(commit=False)
    #     instance.slug = slugify(user.id + instance.title)
    #     instance.save()
    #
    #     return instance
