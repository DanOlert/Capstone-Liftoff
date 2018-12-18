from django.contrib import admin

# Register your models here.
from .models import UserSettings
from .models import UserStats

# Register your models here.
admin.site.register(UserSettings)
admin.site.register(UserStats)
