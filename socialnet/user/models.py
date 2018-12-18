from django.db import models
from django.contrib.auth.models import User
import json

AVAILABILITY = (
    ('free','Free'),
    ('semi','Semi-Free'),
    ('busy','Busy')
)

LEADERSHIP = (
    ('self','I prefer to be the creative leader'),
    ('both', 'I prefer multiple creative sources'),
    ('neutral','I am flexible on creative sources'),
    ('others','I prefer creativity of others')
)

INTERPERSONAL = (
    ('others','I work best with others'),
    ('neutral','I have no preference'),
    ('self','I work Best by myself')
)

ATTITUDE = (
    ('laidback','Anything goes!'),
    ('neutral','I have no preference'),
    ('intense','I have high expectactations')
)

PUNCTUALITY = (
    ('loose','Its ok to miss sessions'),
    ('neutral','It depends on how serious the project is'),
    ('medium','Its ok as long as theres a good reason'),
    ('punctual','Scheduled times should not be missed')
)

#PROMPT: Do you value creativity or technical proficiency more
VALUES = (
    ('creativity','Creativity'),
    ('neutral',"I can't decide"),
    ('technical','Technical Proficiency')
)


# Create your models here.
class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return (self.user.username+"-"+str(self.user.id))

class UserStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    role = models.CharField(max_length=100, null=True, default=None)
    availability = models.CharField(max_length=10, choices=AVAILABILITY, default='free')
    genre = models.CharField(max_length=500, null=True, default=None)
    location = models.CharField(max_length=100, null=True, default=None)
    lookingfor = models.CharField(max_length=500, null=True, default=None)
    seriousness = models.CharField(max_length=30, null=True, default=None)
    experience = models.CharField(max_length=30, null=True, default=None)
    leadership = models.CharField(max_length=30, choices=LEADERSHIP, default=None)
    interpersonal = models.CharField(max_length=30, choices=INTERPERSONAL, default=None)
    attitude = models.CharField(max_length=30, choices=ATTITUDE, default=None)
    punctuality = models.CharField(max_length=30, choices=PUNCTUALITY, default=None)
    values = models.CharField(max_length=30, choices=VALUES, default=None)
    goal = models.CharField(max_length=30, null=True, default=None)


    def set_role(self, x):
        self.role = json.dumps(x)

    def get_role(self):
        return json.loads(self.role)

    def set_genre(self, x):
        self.genre = json.dumps(x)

    def get_genre(self):
        return json.genre(self.role)

    def set_lookingfor(self, x):
        self.lookingfor = json.dumps(x)

    def get_lookingfor(self):
        return json.loads(self.lookingfor)

    def set_seriousness(self, x):
        self.seriousness = json.dumps(x)

    def get_seriousness(self):
        return json.loads(self.seriousness)

    #options something like: fame, money, community, friends, musical growth
    def set_goal(self, x):
        self.goal = json.dumps(x)

    def get_goal(self):
        return json.loads(self.goal)


    def __str__(self):
        return (self.user.username+"-"+str(self.user.id))
