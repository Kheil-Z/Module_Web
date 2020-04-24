from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accueil', views.home),
    path('article/<int:id_article>$', views.view_article, name='afficher_article'),
    path('articles/<int:year>',views.list_articles),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date',views.date_acteulle),
    path('addition/<int:nombre1>/<int:nombre2>/',views.addition),
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>$', views.lire, name='lire'),
    path('contact/', views.nouveau_contact, name='contact'),
    path('voir_contacts/', views.voir_contacts, name='voir_contact'),
]
