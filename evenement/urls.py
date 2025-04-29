from django.urls import path
from .views import afficheFORMEvent,desinscrire,modifier_evenement,event_delete,event_detail,dashbordAdmin,accueil,detail_evenement,desinscription_evenement,inscription_evenement,mesEvenements,enregistrer_evenement

urlpatterns = [
    path('enregistrer_evenement/', enregistrer_evenement, name='enregistrer_evenement'),
    path('accueil/',accueil, name='accueil'),
    path('desinscrire/<int:id>/', desinscrire, name='desinscrire'),
    path('mesEvenements/',mesEvenements, name='mesEvenements'),
    path('inscription_evenement', inscription_evenement, name='inscription_evenement'),
    path('evenement/<int:id>/desinscription/', desinscription_evenement, name='desinscription_evenement'),
    path('evenement/<int:id>/', detail_evenement, name='detail_evenement'),
    path('accueil/',accueil, name='accueil'),
    path('afficheFORMEvent/', afficheFORMEvent, name='afficheFORMEvent'),
    path('evenement/<int:id>/inscription/',inscription_evenement, name='inscription_evenement'),
    path('dashbordAdmin/', dashbordAdmin, name='dashbordAdmin'),
    path('evenement/<int:id>/', event_detail, name='details_evenement'),
path('event/<int:event_id>/delete/', event_delete, name='event_delete'),
path('evenement/modifier/<int:id>/', modifier_evenement, name='modifier_evenement'),


]