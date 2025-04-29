from django.shortcuts import render
from administrateur.models import Utilisateur
from django.contrib import messages
from evenement.models import Evenement
from participation.models import Participation

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Utilisateur


def connexion_utilisateur(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        username = request.POST.get('nom')  # correspond à AbstractUser.username
        adresse = request.POST.get('adresse')
        telephone = request.POST.get('telephone')
        
        utilisateur = Utilisateur(nom=username, telephone=telephone, adresse=adresse, role=role).save() 

        messages.success(request, f"{'Administrateur' if role == 'administrateur' else 'Utilisateur'} créé avec succès")

        if role == 'admin':
            return redirect('dashbord_admin')  # nom de l’url dans urls.py
        else:
            return redirect('accueil')

    return render(request, 'connexion.html')

def dashbordAdmin(request):
    cat = Evenement.objects.count()
    evenements = Evenement.objects.all()
    pat = Participation.objects.count()
    participants = Participation.objects.all()
    return render(request, 'dashbordAdmin.html',{'cat':cat,'pat':pat,'evenements':evenements,'participants':participants})

def verifiCon(request):
    return render(request, 'verifierConnecte.html') 


def verifier_connection(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        telephone = request.POST.get('telephone')
        # Rechercher un événement avec ce nom ET ce téléphone
        evenement = Utilisateur.objects.filter(nom=nom, telephone=telephone).first()
        nap  = Utilisateur.objects.get(nom=nom).role
        utilisateur = Utilisateur.objects.get(nom=nom, telephone=telephone)
        request.session['admin_username'] = utilisateur.nom
        username = request.session.get('admin_username', 'Administrateur')
        request.session['utilisateur_id'] = utilisateur.id
        if nap == 'admin':
            return redirect('dashbord_admin')  
        else:
            return redirect('accueil') 
            return render(request,'accueil.html', {'username': username}) 

    return render(request, 'formulaire.html')

#def accueil(request):
#    evenements  = Evenement.objects.all()
#    return render(request, 'accueil.html', {'evenements': evenements})

def accueil(request):
    evenements  = Evenement.objects.all()
    username = request.session.get('admin_username', None)
    return render(request, 'accueil.html', {'username': username,'evenements': evenements})

