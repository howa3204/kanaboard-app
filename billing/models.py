from django.conf import settings
from django.db import models

# Create your models here.

class StripeCustomer(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=255)
    subscription_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Stripe Customers"

    def __str__(self):
        return self.owner.email
