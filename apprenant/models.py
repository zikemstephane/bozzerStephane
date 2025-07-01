from django.db import models

# Create your models here.
class Apprenant(models.Model):
    id = models.AutoField(primary_key=True)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=15)
    mot_de_passe = models.CharField(max_length=100)
    confirme = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom} {self.prenom}"