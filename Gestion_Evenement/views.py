from django.shortcuts import render,redirect
from evenement.models import Evenement
def Authentification(request):
    return render(request, 'connexion.html')
