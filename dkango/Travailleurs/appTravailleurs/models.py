from django.db import models

# Create your models here.

class Travailleur(models.Model):
    name = models.CharField(max_length=255)
    salaire = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
