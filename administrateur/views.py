from django.shortcuts import render

# Create your views here.
from administrateur.models import Administrateur
from quartier.models import Quartier
from categorie.models import Categorie
from django.contrib import messages
from maison.models import Maison

def formulaireAuthentification(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            admin = Administrateur.objects.get(username=username, password=password)
            messages.success(request, "Connexion réussie ! Bienvenue.")
            request.session['admin_username'] = admin.username
            username = request.session.get('admin_username',None)
            id_admin = Administrateur.objects.get(username=username).id
            piol = Quartier.objects.filter(Administrateur_id=id_admin).all()
            kwatt = Maison.objects.filter(quartier_id__in=piol).count()
            quartiers = Quartier.objects.filter(Administrateur_id=id_admin).count()
            categories = Categorie.objects.all().count()
            return render(request, 'Dashbord.html', {'username': username,'quartiers': quartiers, 'categories': categories, 'kwatt': kwatt})
        except Administrateur.DoesNotExist:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return render(request, 'Authentification.html')
    return render(request, 'Dashbord.html')

#def dashboard(request):
#    username = request.session.get('admin_username', 'Administrateur')
#    return render(request, 'Dashbord.html', {'username': username})