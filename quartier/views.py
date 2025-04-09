from django.shortcuts import render
from django.contrib import messages
def creer_quartier(request):
    return render(request, 'quartier.html')
# Create your views here.
# views.py
from django.shortcuts import render, redirect
from quartier.models import Quartier

def ajouter_quartier(request):
    if request.method == 'POST':
        nom=request.POST['Nom']
        ville=request.POST['ville']
        superficie = request.POST['superficie']
        dernier_quartier = Quartier.objects.last()
        if dernier_quartier:
            dernier_id = dernier_quartier.id+1  
        Quartier(dernier_id,nom,ville,superficie).save()
        messages.success(request, "Le quartier a été enregistré avec succès !")
        return redirect('/quartier')

from django.shortcuts import render
from quartier.models import Quartier

def parcour(request):
    derniers_quartiers = Quartier.objects.all()
    return render(request, 'quartier.html', {'quartiers': derniers_quartiers})
