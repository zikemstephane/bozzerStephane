from django.db import models
from quartier.models import Quartier
from categorie.models import Categorie

# Create your models here.
class Maison(models.Model):
    id = models.AutoField(primary_key=True)
    adresse = models.CharField(max_length=200)
    superficie = models.FloatField()
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE ,default=1)
    type_maison = models.ForeignKey(Categorie, on_delete=models.CASCADE ,default=1)

    def __str__(self):
        return self.username