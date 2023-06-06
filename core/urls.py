""" 
URL configuration for core app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from django.urls import path
from core.views import index, salas, contato, sobre, login, cadastro

urlpatterns = [
	path('', index, name='index'),
	path('salas/', salas, name='salas'),
	path('contato/', contato, name='contato'),
	path('sobre/', sobre, name='sobre'),
	path('login', login, name='login'),
	path('cadastro', cadastro, name='cadastro'),
]