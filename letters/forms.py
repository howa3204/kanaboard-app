from django import forms
from django.forms import ModelForm

from .models import Letter

class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = [
            'letter_title',
            'letter_type',
            'school_association',
            'author_prefix',
            'author_first_name',
            'author_last_name',
            'author_title',
            'organization_name',
            'address',
            'country',
            'city',
            'phone',
            'email',
        ]
