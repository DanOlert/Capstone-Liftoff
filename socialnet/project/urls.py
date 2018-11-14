
from django.urls import path
from django.conf.urls import url
from . import views

app_name='project' #namespaced this app.

urlpatterns = [
    path('', views.project_demo, name="demo"),
    path('new/', views.project_new, name="new"),
    #slug url needs to be last!
    url(r'^(?P<slug>[\w-]+)/$',views.project_detail, name="detail"),
]
