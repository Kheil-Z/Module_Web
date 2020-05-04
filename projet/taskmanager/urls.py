
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('connexion', views.connexion, name='connexion'),
    path('deconnexion', views.deconnexion, name='logout'),
    path('newuser',views.newUser,name="newuser"),
    path('createnewuser', views.createnewUser, name="createnewuser"),
    path('project/<int:id>', views.project, name='project_id'),
    path('projects', views.projects, name='projects'),
    path('task/<int:id1>/<int:id2>', views.task, name='task'),
    path('newtask', views.newtask, name="newtask"),
    path('createnewtask', views.createnewTask, name="createnewtask"),
]
