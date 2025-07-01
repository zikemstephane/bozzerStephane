from django.db import models

# Create your models here.
class Proprietaire(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return self.nom