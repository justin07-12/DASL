from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Register your models here.
class MyUserAdmin(UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm

admin.site.register(User, MyUserAdmin)
