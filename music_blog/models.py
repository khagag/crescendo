from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
#userName=models.OneToOneField(User,on_delete=models.CASCADE)

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
# TODO:  add an image field in here
    # userName=models.OneToOneField(User,on_delete=models.CASCADE)
    # userName = models.CharField(max_length=200,default='',unique=True)
    # password = models.CharField(max_length=200,default='')
    # email = models.EmailField(unique=True,null=True)
    fName = models.CharField(max_length=200,default='')
    mName = models.CharField(max_length=200,blank=True,null=True)
    lName = models.CharField(max_length=200,default='')
    date_of_birth = models.DateField(null=True)
    rule = models.ForeignKey(Rules,null=True,on_delete = models.CASCADE)
    def __str__(self):
        return self.fName+' '+self.lName
