from django.conf import settings
from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return str(self.tag)

    class Meta:
        verbose_name_plural = "Tags"

class Task(models.Model):
    task = models.CharField(max_length=200, blank=False)
    due_date = models.CharField(max_length=200, blank=True)
    PRIORITIES = (
        ('Urgent', 'Urgent'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        )
    priority = models.CharField(max_length=200, choices=PRIORITIES, blank=True)
    COMPLETE = (
        ('Yes', 'Yes'),
        ('No', 'No')
        )
    completed = models.CharField(max_length=20, choices=COMPLETE, blank=True)
    TAGS = (
        ('Activities', 'Activities'),
        ('Coursework', 'Coursework'),
        ('Letters', 'Letters'),
        ('MCAT', 'MCAT'),
        ('Other', 'Other'),
        )
    tag = models.CharField(max_length=20, choices=TAGS, blank=True)
    tray = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.task)

    class Meta:
        verbose_name_plural = "Tasks"
