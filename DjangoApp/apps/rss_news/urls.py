from django.contrib import admin
from django.urls import path, re_path
from DjangoApp.apps.rss_news import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<index>/', views.post),
    path('login', views.login),
    path('signup', views.register),
    path('signup_user', views.signup_user, name='signup_user'),
    path('check_user_name', views.check_user_name, name='check_user_name')
]