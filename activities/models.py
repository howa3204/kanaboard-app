from django.db import models
from django.conf import settings

# Create your models here.

class Activity(models.Model):
    TYPE = (
        ('Artistic Endeavors', 'Artistic Endeavors'),
        ('Community Service/Volunteer - Medical/Clinical', 'Community Service/Volunteer - Medical/Clinical'),
        ('Community Service/Volunteer - Not Medical/Clinical', 'Community Service/Volunteer - Not Medical/Clinical'),
        ('Conferences Attended', 'Conferences Attended'),
        ('Extracurricular Activities', 'Extracurricular Activities'),
        ('Hobbies', 'Hobbies'),
        ('Honors/Awards/Recognitions', 'Honors/Awards/Recognitions'),
        ('Intercollegiate Athletics', 'Intercollegiate Athletics'),
        ('Leadership - Not Listed Elsewhere', 'Leadership - Not Listed Elsewhere'),
        ('Military Service', 'Military Service'),
        ('Other', 'Other'),
        ('Paid Employment - Medical/Clinical', 'Paid Employment - Medical/Clinical'),
        ('Paid Employment - Not Medical/Clinical', 'Paid Employment - Not Medical/Clinical'),
        ('Physician Shadowing/Clinical Observation', 'Physician Shadowing/Clinical Observation'),
        ('Presentations/Posters', 'Presentations/Posters'),
        ('Publications', 'Publications'),
        ('Research/Lab', 'Research/Lab'),
        ('Teaching/Tutoring/Teaching Assistant', 'Teaching/Tutoring/Teaching Assistant'),
    )
    experience_type = models.CharField(max_length=200, choices=TYPE, blank=True)
    experience_name = models.CharField(max_length=200, null=True, blank=True)
    organization_name = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.CharField(max_length=200, null=True, blank=True)
    end_date = models.CharField(max_length=200, null=True, blank=True)
    total_hours = models.FloatField(null=True, blank=True)
    REPEATED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    repeated = models.CharField(max_length=200, choices=REPEATED, blank=True)
    contact_first_name = models.CharField(max_length=200, null=True, blank=True)
    contact_last_name = models.CharField(max_length=200, null=True, blank=True)
    contact_title = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(max_length=200, null=True, blank=True)
    contact_phone = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    experience_description = models.TextField(max_length=700, null=True, blank=True)
    MEANINGFUL = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    most_meaningful = models.CharField(max_length=200, choices=MEANINGFUL, blank=True)
    most_meaningful_summary = models.TextField(max_length=1325, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.experience_name)

    class Meta:
        verbose_name_plural = "activities"
