
from django.urls import path, include
from . import views


urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
]
