from .views import proprietaire,form,inscri_proprietaire,soumettre_annonce
from django.urls import path

urlpatterns = [
    path('proprietaire/',proprietaire,name="proprietaire"),
    path('soumettre_annonce/',soumettre_annonce,name="soumettre_annonce"),
    path('form/',form,name="form"),
    path('inscri_proprietaire/',inscri_proprietaire,name="inscri_proprietaire"),
]