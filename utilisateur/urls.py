from django.contrib import admin
from .views import connexion,inscription,dashbords,dashbordsEtu,envoyer_mot_de_passe
from django.urls import path

urlpatterns = [
    path('connexion/',connexion,name="connexion"),
    path('dashbords/',dashbords,name="dashbords"),
    path('inscription/',inscription,name="inscription"),
    path('dashbordsEtu/',dashbordsEtu,name="dashbordsEtu"),
    path('envoyer_mot_de_passe/', envoyer_mot_de_passe, name='envoyer_mot_de_passe'),
]