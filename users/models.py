from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Privileges(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Rules(models.Model):
    name = models.CharField(max_length=120)
    priv = models.ForeignKey(Privileges,on_delete = models.CASCADE)
    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    rule = models.ForeignKey(Rules,null=True,on_delete = models.CASCADE)
