from django import forms
from django.utils.safestring import mark_safe
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class UserForm(forms.ModelForm):
    email = forms.EmailField()
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']
