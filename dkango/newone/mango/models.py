from django.db import models

# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=30)
    region = models.CharField(max_length=50)
    image = models.TextField()

    def __str__(self):
        return self.name
