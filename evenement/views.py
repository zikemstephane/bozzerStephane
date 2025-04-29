from django.shortcuts import render, redirect
from evenement.models import Evenement
from django.contrib import messages
from participation.models import Participation
from administrateur.models import Utilisateur
from django.shortcuts import render, get_object_or_404





def enregistrer_evenement(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date = request.POST.get('date')
        heure = request.POST.get('heure')
        lieu = request.POST.get('lieu')
        max_participation = request.POST.get('max_participation')
        date_creation = request.POST.get('date_creation')

        even = Evenement(
            titre=titre,
            description=description,
            date=date,
            heure=heure,
            lieu=lieu,
            max_participants=max_participation,
            date_creation=date_creation
        )
        even.save()
        messages.success(request, "Événement créé avec succès !")
        return redirect('dashbord_admin')  # Assure-toi que cette URL existe dans ton `urls.py`

    return render(request, 'dashbordAdmin.html',{'messages':messages.success})

def afficheFORMEvent(request):
    return render(request,'formulaireEvent.html')

def dashbordAdmin(request):
    cat = Evenement.objects.count()
    evenements = Evenement.objects.all()
    pat = Participation.objects.count()
    return render(request, 'dashbordAdmin.html',{'cat':cat,'pat':pat,'evenements':evenements})

def accueil(request):
    username = request.session.get('admin_username', 'Administrateur')
    
    return render(request, 'accueil.html',{'username': username})

def detail_evenement(request, id):
    event = get_object_or_404(Evenement, id=id)
    return render(request, 'detail.html', {'event': event})



def desinscription_evenement(request, id):
    if request.method == 'POST':
        nom = request.session.get('nom')
        telephone = request.session.get('telephone')

        if not nom or not telephone:
            # L'utilisateur n'est pas connecté
            return redirect('connexion_utilisateur')

        evenement = get_object_or_404(Evenement, id=id)

        # Vérifie la participation
        try:
            participation = Participation.objects.get(evenement=evenement, nom=nom, telephone=telephone)
            participation.delete()  # Supprime l’inscription
        except Participation.DoesNotExist:
            pass  # L'utilisateur n'était pas inscrit, on ignore

        return redirect('detail_evenement', id=id)

    # Si ce n’est pas une requête POST, on redirige
    return redirect('detail_evenement', id=id)

from django.shortcuts import render, get_object_or_404, redirect
from administrateur.models import Utilisateur
from evenement.models import Evenement
from participation.models import Participation

def inscription_evenement(request, id):
    if request.method == 'POST':
        date_inscription = request.POST.get('date_inscription')
        nom_utilisateur = request.POST.get('nom_utilisateur')

        if not nom_utilisateur:
            messages.error(request, "Utilisateur non connecté.")
            return redirect('accueil')

        utilisateur = Utilisateur.objects.filter(nom=nom_utilisateur).first()
        if not utilisateur:
            messages.error(request, "Utilisateur introuvable.")
            return redirect('accueil')

        evenement = get_object_or_404(Evenement, id=id)

        deja_inscrit = Participation.objects.filter(evenement=evenement, utilisateur=utilisateur).exists()
        if not deja_inscrit:
            Participation.objects.create(
                evenement=evenement,
                utilisateur=utilisateur,
                date_inscription=date_inscription
            )
            messages.success(request, "Inscription réussie !")
        else:
            messages.warning(request, "Vous êtes déjà inscrit à cet événement.")

        return redirect('accueil')


def mesEvenements(request):
    username = request.session.get('admin_username', None)
    if not username:
        return redirect('connexion_utilisateur')  

    utilisateur = get_object_or_404(Utilisateur, nom=username)

    participations = Participation.objects.filter(utilisateur=utilisateur)
    evenements_participes = Evenement.objects.filter(
        id__in=participations.values_list('evenement_id', flat=True)
    )


    return render(request, 'mes_Evements.html', {
        'username': username,
        'evenements_participes': evenements_participes
    })


def desinscrire(request, id):
    username = request.session.get('admin_username', None)
    
    if not username:
        messages.error(request, "Utilisateur non connecté.")
        return redirect('accueil')
    
    administrateur = get_object_or_404(Utilisateur, nom=username)

    participation = Participation.objects.filter(
        evenement_id=id,         
        utilisateur_id=administrateur.id
    ).first()
    
    if participation:
        participation.delete()
        messages.success(request, "Vous vous êtes désinscrit de l'événement avec succès.")
    else:
        messages.error(request, "Erreur : vous n'êtes pas inscrit à cet événement.")
    
    return redirect('accueil')


def event_detail(request, event_id):
    event = get_object_or_404(Evenement, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def event_delete(request, event_id):
    event = get_object_or_404(Evenement, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('dashbordAdmin')  
    return render(request, 'event_confirm_delete.html', {'event': event})

def modifier_evenement(request, id):
    evenement = get_object_or_404(Evenement, id=id)

    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date = request.POST.get('date')
        heure = request.POST.get('heure')
        lieu = request.POST.get('lieu')
        max_participation = request.POST.get('max_participation')

        evenement.titre = titre
        evenement.description = description
        evenement.date = date
        evenement.heure = heure
        evenement.lieu = lieu
        evenement.max_participants = max_participation
        evenement.save()

        messages.success(request, "L'événement a été modifié avec succès.")
        return redirect('dashbordAdmin')

    return render(request, 'modifier_evenement.html', {'evenement': evenement})



#def enregistrer_evenement(request):
#    if request.method == 'POST':
#        titre = request.POST.get('titre')
#        description = request.POST.get('description')
#        date = request.POST.get('date')
#        heure = request.POST.get('heure')
#        lieu = request.POST.get('lieu')
#        max_participation = request.POST.get('max_participation')
#        date_creation = request.POST.get('date_creation')
#
#        even = Evenement(
#            titre=titre,
#            description=description,
#            date=date,
#            heure=heure,
#            lieu=lieu,
#            max_participants=max_participation,
#            date_creation=date_creation
#        )
#        even.save()
#        message = f"Nouvel événement: {titre} - {description} le {date}"
#        utilisateurs = Utilisateur.objects.all()
#        for utilisateur in utilisateurs:
#            if utilisateur.telephone:
#                envoyer_sms(utilisateur.telephone, message)
#        messages.success(request, "Événement créé avec succès !")
#        return redirect('dashbordAdmin')  # Assure-toi que cette URL existe dans ton `urls.py`
#
#    return render(request, 'dashbordAdmin.html',{'messages':messages.success})