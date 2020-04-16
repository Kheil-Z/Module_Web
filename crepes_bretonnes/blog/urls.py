from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<id_article>',views.view_article),
    path('articles/<int:year>',views.list_articles),
    path('articles/<int:year>/<int:month>', views.list_articles),
]