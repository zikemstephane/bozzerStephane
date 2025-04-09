from django.urls import path
from .views import creer_quartier,ajouter_quartier,parcour

urlpatterns = [
    path('',creer_quartier,name='quartier'),
    path('ajouter_quartier/', ajouter_quartier, name='ajouter_quartier'),
    path('parcour/',parcour,name='parcour')
    #path('lister_quartiers/', lister_quartiers, name='lister_quartiers'),
]
