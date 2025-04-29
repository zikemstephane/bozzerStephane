from django.urls import path
from .views import connexion_utilisateur,dashbordAdmin,verifiCon,verifier_connection,accueil

urlpatterns = [
    path('accueil/',accueil, name='accueil'),
path('admin/dashboard/', dashbordAdmin, name='dashbord_admin'),
    path('verifier_connection/', verifier_connection, name='verifier_connection'),
path('verifiCon', verifiCon, name='verifiCon'),
    path('connexion_utilisateur/', connexion_utilisateur, name='connexion_utilisateur'),
]