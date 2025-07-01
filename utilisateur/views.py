from django.shortcuts import render
from utilisateur.models import Utilisateur
from proprietaire.models import Proprietaire
from etudiant.models import Etudiant
from logement.models import Logement
from django.shortcuts import redirect
from logement.models import LogementImage
from django.conf import settings

from django.core.mail import send_mail
import ssl
import certifi

ssl_context = ssl.create_default_context(cafile=certifi.where())


from django.contrib import messages
# Create your views here.

def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mot_de_passe = request.POST.get('password')
        utilisateur = Proprietaire.objects.filter(email=email, mot_de_passe=mot_de_passe).first() 

        if utilisateur:
            request.session['utilisateur_email'] = utilisateur.email
            messages.success(request, 'Connexion réussie')
            return redirect('dashbords')
        
        utilisateur =  Etudiant.objects.filter(email=email, mot_de_passe=mot_de_passe).first()

        if utilisateur:
            request.session['utilisateur_email'] = utilisateur.email
            messages.success(request, 'Connexion réussie')
            return redirect('dashbordsEtu')
        
    return render(request, 'login.html',{'messages': messages})
        
def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        mot_de_passe = request.POST.get('password')
        userType = request.POST.get('userType')
        filiere = request.POST.get('filiere')
        entreprise = request.POST.get('entreprise')
        matricule = request.POST.get('matricule')

        # Vérifie si l'email est déjà utilisé
        if Proprietaire.objects.filter(email=email).exists() or Etudiant.objects.filter(email=email).exists():
            messages.error(request, 'Cet email est déjà utilisé.')
            return render(request, 'register.html')

        if userType == 'proprietaire':
            prop = Proprietaire(
                nom=nom,
                email=email,
                mot_de_passe=mot_de_passe,
                entreprise=entreprise,
                telephone=telephone
            )
            prop.save()

            # Enregistre en session
            request.session['utilisateur_email'] = email

            messages.success(request, 'Inscription en tant que propriétaire réussie.')
            return redirect('dashbords')  # à remplacer par le nom réel de l'URL

        else:  # étudiant
            etude = Etudiant(
                nom=nom,
                email=email,
                mot_de_passe=mot_de_passe,
                filiere=filiere,
                matricule=matricule
            )
            etude.save()

            request.session['utilisateur_email'] = email

            messages.success(request, 'Inscription en tant qu’étudiant réussie.')
            return redirect('dashbordsEtu')  # à remplacer par le nom réel de l'URL

    return render(request, 'register.html')

def dashbords(request):
    # Récupérer l'email de session
    email = request.session.get('utilisateur_email')
    nom = None
    img = None
    tout = []

    if email:
        # Une seule requête pour récupérer le propriétaire
        utilisateur = Proprietaire.objects.filter(email=email).first()
        if utilisateur:
            nom = utilisateur.nom
            # Récupérer les logements associés à ce propriétaire
            tout = Logement.objects.filter(proprietaire=utilisateur)
            # Récupérer une image associée à un de ses logements
            image = LogementImage.objects.filter(logement__proprietaire=utilisateur).first()
            if image:
                img = image.image.url

    return render(request, 'dashproprio.html', {
        'nom_utilisateur': nom,
        'tout': tout,
        'image': img
    })

def dashbordsEtu(request):
    email = request.session.get('utilisateur_email')
    nom_utilisateur = None

    utilisateur = Etudiant.objects.filter(email=email).first()
    if utilisateur:
        nom_utilisateur = utilisateur.nom

    logements = Logement.objects.all().prefetch_related('images')[:3]

    # Associer la première image à chaque logement pour l’affichage rapide
    for logement in logements:
        logement.premiere_image = logement.images.first()

    return render(request, 'dashetudiantouparent.html', {
        'nom_utilisateur': nom_utilisateur,
        'tout': logements,
        'utilisateur':utilisateur
    })

import smtplib
import ssl
from email.message import EmailMessage
from django.shortcuts import render
from etudiant.models import Etudiant

def envoyer_mot_de_passe(request):
    message = ""

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = Etudiant.objects.get(email=email)

            msg = EmailMessage()
            msg['Subject'] = "Votre mot de passe"
            msg['From'] = "zikemstephane@gmail.com"
            msg['To'] = user.email
            msg.set_content(f"Bonjour {user.nom},\n\nVoici votre mot de passe : {user.mot_de_passe}")

            # ⚠️ Désactivation de la vérification SSL — à ne pas utiliser en production
            context = ssl._create_unverified_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login("zikemstephane@gmail.com", "znghyeokurdjdrea")
                smtp.send_message(msg)

            message = "Mot de passe envoyé avec succès."

        except Etudiant.DoesNotExist:
            message = "Aucun utilisateur avec cet e-mail."

    return render(request, 'mdp oublie.html', {'message': message})
