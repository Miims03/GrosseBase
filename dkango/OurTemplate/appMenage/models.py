from django.db import models

# Create your models here.

class Personne(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    salaire = models.FloatField()

    def __str__(self) -> str:
        return self.name

class Prof(models.Model):
    name = models.CharField(max_length=255)
    cours = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name