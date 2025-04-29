from django.db import models

# Create your models here.
class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.CharField(max_length=255, blank=True)
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('user', 'Utilisateur simple'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username