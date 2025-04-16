from django.db import models
from administrateur.models import Administrateur

# Create your models here.
class Quartier(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    superficie = models.FloatField()
    description = models.CharField(max_length=300)  
    Administrateur = models.ForeignKey(Administrateur, on_delete=models.CASCADE ,default=1)
    
    def __str__(self):
        return self.username