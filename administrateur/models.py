from django.db import models

# Create your models here.
class Administrateur(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  
    
    def __str__(self):
        return self.username