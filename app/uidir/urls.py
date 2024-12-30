"""
This file contains all route and path configurations for the app.
"""

from django.urls import path
from . import views

app_name = 'uidir'

urlpatterns = [
    path('', views.home, name='home'),
    path('consultation/', views.consultation, name='consultation'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
]
