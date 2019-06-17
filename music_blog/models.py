from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

#User data to the

class Privileges(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Rules(models.Model):
    name = models.CharField(max_length=120)
    priv = models.ForeignKey(Privileges,on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class UserInfo(models.Model):
# TODO:  add an image field in here
    # userName=models.OneToOneField(User,on_delete=models.CASCADE)
    # userName = models.CharField(max_length=200,default='',unique=True)
    # password = models.CharField(max_length=200,default='')
    # email = models.EmailField(unique=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fName = models.CharField(max_length=200,default='')
    mName = models.CharField(max_length=200,blank=True,null=True)
    lName = models.CharField(max_length=200,default='')
    date_of_birth = models.DateField(null=True)
    rule = models.ForeignKey(Rules,null=True,on_delete = models.CASCADE)
    def __str__(self):
        return self.fName+' '+self.lName

# composers
class composer(models.Model):
    fName = models.CharField(max_length=200,default='')
    mName = models.CharField(max_length=200,blank=True,null=True)
    lName = models.CharField(max_length=200,default='')
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
# TODO: add __str__(self): for the models

# music date

class music_era(models.Model):
    name = models.CharField(max_length=200,default='')
    start_era = models.DecimalField(max_digits=4,decimal_places=0,null=True)
    end_era = models.DecimalField(max_digits=4,decimal_places=0,null=True,blank=True)
    bc = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class musical_genre(models.Model):
    name = models.CharField(max_length=200,default='')

class scale_type(models.Model):
    name = models.CharField(max_length=200,default='')

class scale(models.Model):
    name = models.CharField(max_length=200,default='')

class musical_piece(models.Model):
    name = models.CharField(max_length=200,default='')
    scale = models.ForeignKey(scale,null=True,on_delete = models.CASCADE)
    type = models.ForeignKey(scale_type,null=True,on_delete = models.CASCADE)
    comp = models.ForeignKey(composer,null=True,on_delete = models.CASCADE)

#user lists
class list(models.Model):
    owner = models.ForeignKey(User,null=True,on_delete = models.CASCADE)
    name = models.CharField(max_length=200,default='')
    description = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class list_content(models.Model):
    list_id = models.ForeignKey(list,null=True,on_delete = models.CASCADE)
    music = models.ForeignKey(musical_piece,null=True,on_delete = models.CASCADE)
