from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)




# from django.contrib import admin
#
# # Register your models here.
# from django.apps import apps
#
# app = apps.get_app_config('music_blog')
#
# for model_name, model in app.models.items():
#     admin.site.register(model)

# from django.apps import apps
#
# models = apps.get_models()
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass
