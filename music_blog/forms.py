"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
"""
""" ########## old code ********************"""

from django import forms
from django.contrib.auth.models import  User
from .models import  UserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_verification = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_verification',
            'email'
        ]

        widgets = {

        }
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = [
            'fName',
            'lName'
        ]
        labels = {
            'fName' : 'First name',
            'lName' : 'Last name'
        }
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
