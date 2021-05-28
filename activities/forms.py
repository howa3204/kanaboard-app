from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = [
            'experience_type',
            'experience_name',
            'organization_name',
            'start_date',
            'end_date',
            'total_hours',
            'repeated',
            'contact_first_name',
            'contact_last_name',
            'contact_title',
            'contact_email',
            'contact_phone',
            'city',
            'country',
            'experience_description',
            'most_meaningful',
            'most_meaningful_summary',
        ]
