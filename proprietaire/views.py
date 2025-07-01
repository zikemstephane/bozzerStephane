from django.shortcuts import render
from proprietaire.models import Proprietaire
from django.contrib import messages


# Create your views here.
def proprietaire(request):
    return render(request,'proprietaireCon.html')

def form(request):
    return render(request,'form.html')

def inscri_proprietaire(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        password = request.POST.get('mot_de_passe')
        entreprise = request.POST.get('entreprise')
        telephone = request.POST.get('telephone')
        enre = Proprietaire(nom=nom,email=email,mot_de_passe=password,entreprise=entreprise,telephone=telephone)
        enre.save()
        messages.success(request,"Inscription en tant que proprietaire reussie")
        return render(request,'proprietaireCon.html',{'message':messages})
    return render(request,'proprietaireCon.html',{'message':messages})

def soumettre_annonce(request):
    return render(request,'soumettre-annonce.html')