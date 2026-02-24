from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Message
from .forms import MessageForm
from administrateur.models import Utilisateur  

@login_required
def chatbox(request, destinataire_id):
    destinataire = Utilisateur.objects.get(id=destinataire_id)
    
    messages = Message.objects.filter(
        (Q(expediteur=request.user) & Q(destinataire=destinataire)) |
        (Q(expediteur=destinataire) & Q(destinataire=request.user))
    ).order_by('date_envoi')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.expediteur = request.user
            message.destinataire = destinataire
            message.save()
            return redirect('chatbox', destinataire_id=destinataire.id)
    else:
        form = MessageForm()

    return render(request, 'chatbox.html', {
        'form': form,
        'messages': messages,
        'destinataire': destinataire
    })


def chatboxe(request):
    return render(request,'chatbox.html')