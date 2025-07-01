from django.db import models
from logement.models import Logement
from etudiant.models import Etudiant

# Create your models here.
class Avis(models.Model):
    id = models.AutoField(primary_key=True)
    commentaire = models.TextField()
    note = models.IntegerField()
    datePublication = models.DateTimeField(auto_now_add=True)
    logement_id = models.ForeignKey(Logement, on_delete=models.CASCADE, null=True, blank=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, null=True, blank=True)

def __str__(self):
    return f"Avis {self.id} - Note: {self.note}"