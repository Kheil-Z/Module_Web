
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('album/<int:id>', views.album, name='afficher_album'),
    path('q/request', views.query, name='query')
]
