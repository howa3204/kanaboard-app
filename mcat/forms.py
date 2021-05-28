from django import forms
from django.forms import ModelForm

from .models import MCAT

class MCATForm(ModelForm):
    class Meta:
        model = MCAT
        fields = [
            'test_date',
            'test_company',
            'test_type',
            'test_name',
            'bio_biochem',
            'chem_physics',
            'psych_soc',
            'cars',
        ]
