
from django.urls import path
from django.conf.urls import url
from . import views

app_name='posts' #namespaced this app.

urlpatterns = [
    path('', views.post_list, name="list"),
    path('new/', views.post_new, name="new"),
    #slug url needs to be last!
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="detail"),
]
