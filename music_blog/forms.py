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

""" ########## old code ********************"""

# from django import forms
# from .models import User

# class RegistForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'password',
#             'fName',
#             'lName',
#             'Rule'
#         ]

# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
