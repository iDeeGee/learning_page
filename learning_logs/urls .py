"""Определяем схемы URL для learning logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name = 'index')
]