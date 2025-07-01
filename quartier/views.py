from django.shortcuts import render
from django.contrib import messages
from quartier.models import Quartier
from administrateur.models import Administrateur
from categorie.models import Categorie
from maison.models import Maison
from django.shortcuts import get_object_or_404, redirect

def quartier(request):
    if request.method == "POST":
        nom_quartier = request.POST.get("nom")
        superficie = request.POST.get("superficie")
        description = request.POST.get("description")
        administrateur = request.POST.get("administrateur")
        quart = Administrateur.objects.get(username=administrateur).id
        try:
            quartier = Quartier(nom=nom_quartier, superficie=superficie, description=description,Administrateur_id = quart)
            quartier.save()
            messages.success(request, "Quartier ajouté avec succès !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'ajout du quartier : {e}")
    return render(request, 'FormQuartier.html',{'message': messages.get_messages(request)})

def formQuartier(request):
    username = request.session.get('admin_username', None)
    return render(request, 'formQuartier.html',{'username':username})

def Dashbord(request):
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).count()
    piol = Quartier.objects.filter(Administrateur_id=id_admin).all()
    kwatt = Maison.objects.filter(quartier_id__in=piol).count()
    categories = Categorie.objects.all().count()
    return render(request, 'Dashbord.html', {'username': username, 'quartiers': quartiers, 'categories': categories, 'kwatt': kwatt})


def listerQuartier(request):
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).all()
    quart = Quartier.objects.filter(Administrateur_id=id_admin).all().count()
    if(quart==0):
        messages.success(request, "Vous n'avez aucune maison pour le momemt.")
        return render(request, 'quartier.html', {'quartiers': quartiers, 'username': username,'message': messages.get_messages(request)})
    else:
        return render(request, 'quartier.html', {'quartiers': quartiers, 'username': username})

def supprimerQuartier(request, id):
    quartier = get_object_or_404(Quartier, id=id)
    quartier.delete()
    messages.success(request, "Quartier supprimée avec succès.")
    return redirect('listerQuartier')

def modifierQuartier(request, id):
    quartier = get_object_or_404(Quartier, id=id)
    if request.method == "POST":
        quartier.nom = request.POST.get('nom')
        quartier.description = request.POST.get('description')
        quartier.superficie = request.POST.get('superficie')
        quartier.save()
        messages.success(request, "Quartier modifiée avec succès.")
        return redirect('listerQuartier')
    return render(request, 'modifierQuartier.html', {'quartier': quartier})
