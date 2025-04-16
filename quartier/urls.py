from django.urls import path
from .views import quartier,formQuartier,Dashbord,listerQuartier,supprimerQuartier,modifierQuartier

urlpatterns = [
    path('quartier/', quartier, name='quartier'),
    path('listerQuartier/', listerQuartier, name='listerQuartier'),
    path('supprimerQuartier/<int:id>/', supprimerQuartier, name='supprimerQuartier'),
    path('modifierQuartier/<int:id>/', modifierQuartier, name='modifierQuartier'),
    path('formQuartier/', formQuartier, name='formQuartier'),
    path('Dashbord/',Dashbord,name='Dashbord')
]