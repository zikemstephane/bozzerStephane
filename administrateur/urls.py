from django.urls import path
from .views import formulaireAuthentification#,dashboard

urlpatterns = [
    path('formulaireAuthentification/', formulaireAuthentification, name='formulaireAuthentification'),
    #path('dashbord/', dashboard, name='dashboard'),

]