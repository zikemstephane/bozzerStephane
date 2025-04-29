from django.db import models
from administrateur.models import Utilisateur
from evenement.models import Evenement

# Create your models here.
class Participation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilisateur', 'evenement')  # Un utilisateur ne peut s’inscrire qu’une fois à un événement

    def __str__(self):
        return f"{self.utilisateur.username} participe à {self.evenement.titre}"
