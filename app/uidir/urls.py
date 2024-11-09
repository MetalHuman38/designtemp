"""
This file contains all route and path configurations for the app.
"""

from django.urls import path
from . import views

app_name = 'uidir'

urlpatterns = [
    path('', views.home, name=''),
]
