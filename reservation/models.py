from django.db import models
from etudiant.models import Etudiant
from logement.models import Logement

# Create your models here.
class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    dateDemande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=100)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True)
    logement_id = models.ForeignKey(Logement, on_delete=models.CASCADE, null=True, blank=True)