from django import forms
from django.forms import ModelForm

from registration.models import CustomUser, Profile

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]
