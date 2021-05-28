from django import forms
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.forms import ModelForm

from activities.models import Activity

class QuickForm(forms.Form):
    experience_name = forms.ModelChoiceField(queryset=Activity.objects.all(), required=True)
    hours = forms.FloatField(validators=[MinValueValidator(0)], required=True)
