from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def mwp(request):
    return render(request, 'mdp oublie.html')

def apropos(request):
    return render(request, 'apropos.html')

def principe(request):
    return render(request, 'frontend.html')