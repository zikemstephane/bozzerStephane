from django.urls import path
from .views import formCategorie,Dashbord,enregistreCategorie,listerCategorie,supprimerCategorie,modifierCategorie

urlpatterns = [
    path('formCategorie/', formCategorie, name='formCategorie'),
    path('modifierCategorie/<int:id>/', modifierCategorie, name='modifierCategorie'),
    path('supprimerCategorie/<int:id>/', supprimerCategorie, name='supprimerCategorie'),
    path('listerCategorie/', listerCategorie, name='listerCategorie'),
    path('enregistreCategorie/', enregistreCategorie, name='enregistreCategorie'),
    path('Dashbord/',Dashbord,name='Dashbord')
]