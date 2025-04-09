from django.db import models
class Quartier(models.Model):
    id = models.AutoField(primary_key=True)
    nom_quartier = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    superficies = models.FloatField()
    def __str__(self):
         return self.nom_quartier
# Create your models here.

