
from django.urls import path
from django.conf.urls import url
from . import views

app_name='apis' #namespaced this app.

urlpatterns = [
    path('', views.api_list, name="list"),
    path('spotify/', views.spotify, name="spotify"),
    path('soundcloud/', views.soundcloud, name="soundcloud"),
]
