from django.shortcuts import render
from quartier.models import Quartier
from categorie.models import Categorie
from maison.models import Maison
from django.contrib import messages
from administrateur.models import Administrateur
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum
from django.core.exceptions import ValidationError


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
    categories = Categorie.objects.all()
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).all()
    if request.method == "POST":
        adresse = request.POST.get("adresse")
        superficie = float(request.POST.get("superficie"))
        nom_quartier = request.POST.get("quartier")
        categorie = request.POST.get("categorie")


        try:
            quartier = Quartier.objects.get(nom=nom_quartier)
            categorie_obj = Categorie.objects.get(Type_maison=categorie)

            # Superficie du quartier
            superficie_quartier = quartier.superficie

            # Superficie déjà utilisée dans ce quartier
            superficie_utilisee = Maison.objects.filter(quartier=quartier).aggregate(
                total=Sum('superficie')
            )['total'] or 0.0

            # Superficie restante
            superficie_restante = superficie_quartier - superficie_utilisee

            # Vérifications
            if superficie > superficie_quartier:
                messages.error(request, "La superficie de cette maison est plus grande que la superficie totale du quartier.")
            elif superficie > superficie_restante:
                messages.error(request, f"Pas assez d'espace disponible dans ce quartier. Il reste seulement {superficie_restante} m².")
            else:
                maison = Maison(
                    adresse=adresse,
                    superficie=superficie,
                    quartier=quartier,
                    type_maison=categorie_obj
                )
                maison.save()
                messages.success(request, "Maison ajoutée avec succès !")

        except Quartier.DoesNotExist:
            messages.error(request, "Quartier introuvable.")
        except Categorie.DoesNotExist:
            messages.error(request, "Catégorie introuvable.")
        except Exception as e:
            messages.error(request, f"Erreur : {e}")

    return render(request, 'FormMaison.html',{'message': messages.get_messages(request), 'quartiers': quartiers, 'categories': categories})

def listerMaison(request):
    username = request.session.get('admin_username', None)
    id_admin = Administrateur.objects.get(username=username).id
    quartiers = Quartier.objects.filter(Administrateur_id=id_admin).all()
    maisons = Maison.objects.filter(quartier_id__in=quartiers).all()
    mais = Maison.objects.filter(quartier_id__in=quartiers).all().count()
    if(mais==0):
        messages.error(request, "Vous ne possedez aucune maison pour le moment monsieur")
        return render(request, 'Maison.html', { 'username': username,'message': messages.get_messages(request)})
    else:
        messages.error(request, "Voici la liste des maisons que vous avez MR ")
        return render(request, 'Maison.html', {'maisons': maisons, 'quartiers': quartiers, 'username': username,'message': messages.get_messages(request)})
 
        

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


    