from django.shortcuts import render,redirect
from django.contrib import messages
from maison.models import Maison
from quartier.models import Quartier
from django.db.models import Sum

def creer_maison(request):
    return render(request, 'maison.html')

def ajouter_maison(request):
    if request.method == 'POST':
        couleur = request.POST['couleur']
        adresse = request.POST['adresse']
        nom = request.POST['kwat']
        quart = Quartier.objects.get(nom_quartier=nom).id
        type=request.POST['type_maison']
        douche = request.POST['nombre_douche']
        superficie = request.POST['superficie']
        dernier_quartier = Maison.objects.last()

        if dernier_quartier:
            dernier_id = dernier_quartier.id+1

        try:
            superficie = float(request.POST['superficie'])
        except ValueError:
            messages.error(request, "La superficie doit être un nombre valide.")
            return redirect('/maison')

        try:
            quartier = Quartier.objects.get(nom_quartier=nom)
        except Quartier.DoesNotExist:
            messages.error(request, "Le quartier sélectionné n'existe pas.")
            return redirect('/maison')

        # Calculer la superficie totale des maisons existantes dans le quartier
        superficies_existantes = Maison.objects.filter(quartier=quartier).aggregate(total_superficie=Sum('superficie'))['total_superficie'] or 0.0

        # Vérifier si la superficie totale dépasse celle du quartier
        if superficies_existantes + superficie > quartier.superficies:
            messages.error(request, "Il n'y a pas assez de place pour créer cette maison.")
        else:
            Maison(dernier_id,couleur,adresse,quart,superficie,type,douche).save()
            messages.success(request, "La maison a été enregistré avec succès !")
            return redirect('/maison')
        return render(request, 'maison.html') 
    

def lister_quartiers(request):
    quartiers = Maison.objects.all()
    step = Quartier.objects.all()
    return render(request, 'maison.html', {'quartiers': quartiers,'course':step})



