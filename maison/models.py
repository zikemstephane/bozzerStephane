from django.db import models 
from quartier.models import Quartier
class Maison(models.Model):
    id = models.AutoField(primary_key=True)
    coleur = models.CharField(max_length=50)
    adresse = models.CharField(max_length=30)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE ,default=1)
    superficie = models.FloatField()
    type_maison = models.CharField(max_length=40)
    nombre_douche = models.IntegerField()


#User.object.setObject
# Create your models here.