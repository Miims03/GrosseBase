from django.db import models

# Create your models here.
class myStudents(models.Model):
    name=models.CharField(max_length=60)
    age=models.IntegerField()
    bourse=models.IntegerField() 

    def __str__(self):
        return self.name   