# models.py
from django.db import models
from participation.models import Participation
from administrateur.models import Utilisateur
from django.contrib.auth.models import User

class Message(models.Model):
    expediteur = models.ForeignKey(Participation, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinataire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='messages_recus')
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expediteur.username} → {self.destinataire.username} : {self.contenu[:20]}"
