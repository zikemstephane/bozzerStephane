from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
def __str__(self):
    return f"{self.nom} {self.prenom}"