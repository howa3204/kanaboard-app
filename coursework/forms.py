from django import forms
from django.forms import ModelForm

from .models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'academic_year',
            'academic_term',
            'school_year',
            'course_number',
            'course_name',
            'course_classification',
            'credit_hours',
            'transcript_grade',
            'include_lab',
        ]
