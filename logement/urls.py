from .views import cree_annonce,supprimer_logement,modifier_logement,detail_annonce,voir_annonces
from django.urls import path

urlpatterns = [
    path('cree_annonce/',cree_annonce,name="cree_annonce"),
path('supprimer_logement/<int:id>/', supprimer_logement, name='supprimer_logement'),
path('modifier_logement/<int:id>/', modifier_logement, name='modifier_logement'),
    path('detail_annonce/<int:id>/', detail_annonce, name='detail_annonce'),
    path('voir_annonces/<int:id>/', voir_annonces, name='voir_annonces'),
]