from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class DjServices(models.Model):
    dj_service_name = models.CharField(max_length=250, blank=True, null=True)
    dj_service_description = models.CharField(max_length=250, blank=True, null=True)
    dj_fully_booked = models.BooleanField(default=False)

    class Meta:
        verbose_name = "DJ Service"
        verbose_name_plural = "DJ Services"

    def __str__(self) -> str:
        return self.dj_service_name
