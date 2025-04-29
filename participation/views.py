from django.shortcuts import render
from evenement.models import Evenement
from django.shortcuts import get_object_or_404


# Create your views here.
def participer(request,id):
    username = request.session.get('admin_username', None)
    # Récupérer l'événement correspondant à l'ID
    eveneme = get_object_or_404(Evenement, id=id)
    evenements = Evenement.objects.all()
    return render(request,'participer.html',{'evenements':evenements,'eveneme':eveneme,'username':username})

def liste_participants(request):
    evenements = Evenement.objects.all() 
    return render(request, 'liste_participants.html', {'evenements': evenements})