from django.db import models

# Create your models here.

class Evenement(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=100)
    max_participants = models.PositiveIntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} - {self.date} à {self.heure}"