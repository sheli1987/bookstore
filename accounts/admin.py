from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models, forms


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    model = models.CustomUser
    form = forms.CustomUserChangeForm
    add_form = forms.CustomUserCreationForm
    list_display = ['email', 'username', ]