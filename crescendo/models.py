from django.db import models

class Comboser(models.Model):
    FName = models.CharField(max_length=50)
    MName = models.CharField(max_length=50)
    LName = models.CharField(max_length=50)
    BirthDate = models.DateField()
