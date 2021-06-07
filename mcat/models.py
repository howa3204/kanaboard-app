from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class MCAT(models.Model):
    test_date = models.CharField(max_length=10)
    COMPANY = (
        ('AAMC', 'AAMC'),
        ('Altius', 'Altius'),
        ('Blueprint', 'Blueprint'),
        ('Gold Standard', 'Gold Standard'),
        ('Kaplan', 'Kaplan'),
        ('Magoosh', 'Magoosh'),
        ('McGraw Hill', 'McGraw Hill'),
        ('The Princeton Review', 'The Princeton Review'),
        ('Other', 'Other'),
        )
    test_company = models.CharField(max_length=20, choices=COMPANY)
    TEST = (
        ('Official', 'Official'),
        ('Practice', 'Practice'),
        )
    test_type = models.CharField(max_length=8, choices=TEST)
    test_name = models.CharField(max_length=80, blank=True)
    bio_biochem = models.PositiveIntegerField(validators=[MinValueValidator(118), MaxValueValidator(132)])
    chem_physics= models.PositiveIntegerField(validators=[MinValueValidator(118), MaxValueValidator(132)])
    psych_soc = models.PositiveIntegerField(validators=[MinValueValidator(118), MaxValueValidator(132)])
    cars = models.PositiveIntegerField(validators=[MinValueValidator(118), MaxValueValidator(132)])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mcat_score =  models.PositiveIntegerField(validators=[MinValueValidator(472), MaxValueValidator(528)], default=528)

    def save(self, *args, **kwargs):
        self.mcat_score = self.bio_biochem + self.chem_physics + self.psych_soc + self.cars
        super(MCAT, self).save(*args, **kwargs)
        return self.mcat_score

    def __str__(self):
        return str(self.test_date)

    class Meta:
        verbose_name_plural = "MCAT"
