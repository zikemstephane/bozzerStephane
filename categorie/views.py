from django.shortcuts import render
from categorie.models import Categorie
from django.contrib import messages
from quartier.models import Quartier
from maison.models import Maison
from django.shortcuts import get_object_or_404, redirect
from administrateur.models import Administrateur

# Create your views here.
def formCategorie(request):
    return render(request,'FormCategorie.html')

def Dashbord(request):
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).count()
    piol = Quartier.objects.filter(Administrateur_id=id_admin).all()
    kwatt = Maison.objects.filter(quartier_id__in=piol).count()
    Categories = Categorie.objects.all().count()
    return render(request, 'Dashbord.html', {'username': username, 'quartiers': quartiers, 'Categories': Categories, 'kwatt': kwatt})

def enregistreCategorie(request):
    if request.method == "POST":
        nom_categorie = request.POST.get("nom")
        description = request.POST.get("description")
        try:
            categorie = Categorie(Type_maison=nom_categorie, description=description)
            categorie.save()
            messages.success(request, "Catégorie ajoutée avec succès !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'ajout de la catégorie : {e}")
    return render(request, 'FormCategorie.html')

def listerCategorie(request):
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).count()
    piol = Quartier.objects.filter(Administrateur_id=id_admin).all()
    kwatt = Maison.objects.filter(quartier_id__in=piol).count()
    categories = Categorie.objects.all()
    return render(request, 'categorie.html', {'categories': categories, 'username': username, 'quartiers': quartiers, 'kwatt': kwatt})

def supprimerCategorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    categorie.delete()
    messages.success(request, "Catégorie supprimée avec succès.")
    return redirect('listerCategorie')

def modifierCategorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == "POST":
        categorie.nom = request.POST.get('nom')
        categorie.description = request.POST.get('description')
        categorie.save()
        messages.success(request, "Catégorie modifiée avec succès.")
        return redirect('listerCategorie')
    return render(request, 'modifierCategorie.html', {'categorie': categorie})