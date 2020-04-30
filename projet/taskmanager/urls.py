
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='logout'),
    path('tasks', views.tasks, name='tasks'),
]
