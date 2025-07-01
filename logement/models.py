from django.db import models

class Logement(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    surface = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    meublement = models.BooleanField(default=False)
    proprietaire = models.ForeignKey('proprietaire.Proprietaire', on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class LogementImage(models.Model):
    logement = models.ForeignKey(Logement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='logement_images/')

    def __str__(self):
        return f"Image for {self.logement.titre}"
