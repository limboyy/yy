from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'numerical/', views.numerical, name='numerical'),
]