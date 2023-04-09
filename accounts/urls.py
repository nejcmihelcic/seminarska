"""Urls for account related things"""
from django.urls import path, include
from . import views

app_name='accounts'
urlpatterns = [
    #include default auth urls
    path('', include('django.contrib.auth.urls')),
]
