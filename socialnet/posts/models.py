from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    #Not Migrated: use makemigrations to remake this with new thing
    #add in thumbnail
    #and author

    def __str__(self):
        return self.title
