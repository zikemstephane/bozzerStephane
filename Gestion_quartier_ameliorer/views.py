from django.shortcuts import render
def Authentification(request):
    return render(request, 'Authentification.html')

from administrateur.models import Administrateur
from django.contrib import messages
from quartier.models import Quartier

def formulaireAuthentification(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            admin = Administrateur.objects.get(username=username, password=password)
            messages.success(request, "Connexion réussie ! Bienvenue.")
            request.session['admin_username'] = admin.username
            username = request.session.get('admin_username', 'Administrateur')
            id_admin = Administrateur.objects.get(username=username).id
            quartiers = Quartier.objects.filter(Administrateur_id=id_admin).count()

            return render(request, 'Dashbord.html', {'username': username,'quartiers': quartiers})
        except Administrateur.DoesNotExist:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return render(request, 'Authentification.html')
    return render(request, 'Dashbord.html')


