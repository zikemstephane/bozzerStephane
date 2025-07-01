from django.urls import path
from .views import formulaireAuthentification,deconnection

urlpatterns = [
    path('formulaireAuthentification/', formulaireAuthentification, name='formulaireAuthentification'),
    path('', deconnection, name='deconnection'),

]