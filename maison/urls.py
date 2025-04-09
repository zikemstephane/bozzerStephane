from django.urls import path
from .views import ajouter_maison,creer_maison,lister_quartiers

urlpatterns = [
    path('',creer_maison,name='maison'),
    path('ajouter_maison/',ajouter_maison,name='ajouter_maison'),
    path('lister_quartiers/',lister_quartiers,name='lister_quartiers'), 
]

