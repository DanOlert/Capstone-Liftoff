
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/',views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('edit-my-page/', views.edit_my_page, name="edit"),
    path('my_page/', views.my_page, name="mypage"),
    path('<slug>/', views.page_view, name="view"),
    path('<slug>/projects/', views.page_view_projects, name="projects"),

]
