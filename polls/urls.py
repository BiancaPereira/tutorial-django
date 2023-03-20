# Isso é uma URLconf, serve para mapear as URLs

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
