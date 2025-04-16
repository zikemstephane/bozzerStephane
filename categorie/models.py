from django.db import models

# Create your models here.
class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    Type_maison = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.username