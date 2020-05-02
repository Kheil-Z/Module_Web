
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='logout'),
    path('newuser',views.newUser,name="newuser"),
    path('createnewuser', views.createnewUser, name="createnewuser"),
    path('project/<int:id>', views.project, name='project_id'),
    path('tasks', views.tasks, name='tasks'),
]
