from django.db import models
from django.contrib.auth.models import User
from pages.models import Page


POST_TYPE = (
    ('general','General'),
    ('recommendation','Listen to This'),
    ('recommend me','Recommend Me...'),
    ('shows','Live Shows'),
    ('personal', 'Personal'),
    ('new music','Made This!'),
)

PRIVACY = (
    ('none','Everyone'),
    ('friendsoffriends','Friends of Friends'),
    ('friends','Just Friends'),
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    type = models.CharField(max_length=20, choices=POST_TYPE, default='general')
    privacy= models.CharField(max_length=20, choices=PRIVACY, default='none')
    page = models.ForeignKey(Page, null=True, on_delete=models.SET_DEFAULT, default=None)
    body = models.TextField(max_length=2500)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    authorslug = models.CharField(max_length=500, default="missing")
    musicembed = models.CharField(max_length=1500, null=True, blank=True, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:222]
