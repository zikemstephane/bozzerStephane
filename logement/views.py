from django.shortcuts import render
from logement.models import Logement
from proprietaire.models import Proprietaire
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from logement.models import LogementImage
from utilisateur.models import Utilisateur



def cree_annonce(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        if len(images) < 3:
            messages.error(request, "Veuillez sélectionner au moins 3 images.")
            return render(request, 'soumettre-annonce.html')

        titre = request.POST.get('title')
        type_logement = request.POST.get('type')
        surface = request.POST.get('surface')
        meubles = request.POST.get('furnished') == 'on'
        prix = request.POST.get('price')
        adresse = request.POST.get('address')
        description = request.POST.get('description')
        
        email = request.session.get('utilisateur_email')
        proprietaire = Proprietaire.objects.filter(email=email).first()

        if not proprietaire:
            messages.error(request, "Utilisateur non reconnu.")
            return render(request, 'soumettre-annonce.html')

        logement = Logement.objects.create(
            titre=titre,
            description=description,
            adresse=adresse,
            type=type_logement,
            prix=prix,
            surface=surface,
            meublement=meubles,
            proprietaire=proprietaire
        )

        for image in images:
            LogementImage.objects.create(logement=logement, image=image)

        messages.success(request, "Annonce créée avec succès.")
        return render(request, 'soumettre-annonce.html', {'message': messages})
    return render(request, 'soumettre-annonce.html')


def supprimer_logement(request,id):
    logement = get_object_or_404(Logement, id=id)
    if logement:
        logement.delete()
        return render(request, 'dashproprio.html', {'message': 'Logement supprimé avec succès'})
    else:
        return render(request, 'dashproprio.html', {'message': 'Logement non trouvé'})

def modifier_logement(request, id):
    logement = get_object_or_404(Logement, id=id)

    if request.method == 'POST':
        # Récupération des données du formulaire
        images = request.FILES.getlist('images')
        titre = request.POST.get('title')
        type_logement = request.POST.get('type')
        surface = request.POST.get('surface')
        meubles = request.POST.get('furnished') == 'on'
        prix = request.POST.get('price')
        adresse = request.POST.get('address')
        description = request.POST.get('description')

        # Mise à jour du logement
        logement.titre = titre
        logement.type = type_logement
        logement.surface = surface
        logement.meublement = meubles
        logement.prix = prix
        logement.adresse = adresse
        logement.description = description
        logement.save()

        LogementImage.objects.filter(logement=logement).delete()
        # Ajout des nouvelles images (attention : les anciennes ne sont pas supprimées ici)
        for image in images:
            LogementImage.objects.create(logement=logement, image=image)

        messages.success(request, "Logement modifié avec succès.")
        return redirect('modifier_logement', id=logement.id)  # Redirection après succès

    # Si GET, afficher le formulaire avec les données existantes
    return render(request, 'modifier.html', {'logement': logement})

def detail_annonce(request, id):
    logement = get_object_or_404(Logement, id=id)
    idl = logement.proprietaire_id
    lol = logement.prix
    nom_proprietaire = Proprietaire.objects.get(id=idl).nom
    proprietaire = logement.proprietaire

    tous_logements = Logement.objects.filter(prix=lol).exclude(id=logement.id)

    # Récupérer toutes les images du logement actuel
    images_logement = LogementImage.objects.filter(logement=logement)

    # Récupérer la première image du logement (s'il y en a)
    premiere_image = images_logement.first()

    # Optionnel : associer la première image à chaque logement similaire
    for log in tous_logements:
        log.premiere_image = LogementImage.objects.filter(logement=log).first()

    return render(request, 'frontend-detail.html', {
        'comme': logement,
        'toute': tous_logements,
        'images_logement': images_logement,  # toutes les images
        'premiere_image': premiere_image,    # première image
        'proprietaire': nom_proprietaire,
    })




def voir_annonces(request,id):
    logements = get_object_or_404(Logement, id=id)
    images = LogementImage.objects.filter(logement=logements)
    return render(request, 'detail-annonce.html', {'logements': logements,'imagese': images})