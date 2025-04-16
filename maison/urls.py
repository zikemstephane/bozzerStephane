from django.urls import path
from .views import formMaison ,retour,enregistrerMaison,listerMaison,supprimerMaison,modifierMaison

urlpatterns = [
    path('retour/', retour, name='retour'),
    path('supprimerMaison/<int:maison_id>/', supprimerMaison, name='supprimerMaison'),
    path('modifierMaison/<int:maison_id>/', modifierMaison, name='modifierMaison'),
    path('listerMaison/', listerMaison, name='listerMaison'),
    path('formMaison/', formMaison, name='formMaison'),
    path('enregistrerMaison/',enregistrerMaison,name='enregistrerMaison')
]