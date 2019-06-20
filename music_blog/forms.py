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
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  UserInfo

class UserForm(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    # password_verification = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            'email'
        ]

        widgets = {

        }
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = [
            'profile_pic',
        ]
        labels = {
            'profile_pic' : 'Profile picture',
        }
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
