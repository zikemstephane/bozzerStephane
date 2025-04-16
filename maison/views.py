from django.shortcuts import render
from quartier.models import Quartier
from categorie.models import Categorie
from maison.models import Maison
from django.contrib import messages
from administrateur.models import Administrateur
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum


# Create your views here.
def formMaison(request):
    categories = Categorie.objects.all()
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).all()
    return render(request,"FormMaison.html",{'quartiers': quartiers, 'categories': categories})

def retour(request):
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).count()
    piol = Quartier.objects.filter(Administrateur_id=id_admin).all()
    kwatt = Maison.objects.filter(quartier_id__in=piol).count()
    categories = Categorie.objects.all().count()
    return render(request, 'Dashbord.html', {'username': username, 'quartiers': quartiers, 'categories': categories, 'kwatt': kwatt})

def enregistrerMaison(request):
    if request.method == "POST":
        adress = request.POST.get("adresse")
        superficie = request.POST.get("superficie")
        nom_quartier = request.POST.get("quartier")
        categorie = request.POST.get("categorie")
        kwatt = Quartier.objects.get(nom=nom_quartier).id
        piol = Categorie.objects.get(Type_maison=categorie).id
        superficies_existantes = Maison.objects.filter(quartier=nom_quartier).aggregate(total_superficie=Sum('superficie'))['total_superficie'] or 0.0
        try:
            
            maison = Maison(adresse=adress, superficie=superficie, quartier_id=kwatt, type_maison_id=piol)
            maison.save()
            messages.success(request, "Maison ajoutée avec succès !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'ajout de la maison : {e}")
    return render(request, 'FormMaison.html')

def listerMaison(request):
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).all()
    maisons = Maison.objects.filter(quartier_id__in=quartiers).all()
    return render(request, 'Maison.html', {'maisons': maisons, 'quartiers': quartiers, 'username': username})

def supprimerMaison(request, maison_id):
    maison = get_object_or_404(Maison, id=maison_id)
    maison.delete()
    messages.success(request, "Maison supprimée avec succès.")
    return redirect('listerMaison')

def modifierMaison(request, maison_id):
    maison = get_object_or_404(Maison, id=maison_id)
    categories = Categorie.objects.all()
    admin_id = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=admin_id).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).all()

    if request.method == "POST":
        maison.adresse = request.POST.get('adresse')
        maison.quartier_id = request.POST.get('quartier')  
        maison.superficie = request.POST.get('superficie')
        maison.type_maison_id = request.POST.get('categorie')  
        maison.save()
        messages.success(request, "Maison modifiée avec succès.")
        return redirect('listerMaison')

    return render(request, 'ModifierMaison.html', {
        'maison': maison,
        'categories': categories,
        'quartiers': quartiers
    })