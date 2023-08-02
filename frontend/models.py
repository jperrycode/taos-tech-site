from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.crypto import get_random_string


CONTACT_SUBJECT_CHOICES = [
    ("Website Issue", "Website Issue"),
    ("Website Consult","Website Consult"),
    ("Ecommerce Consult", "Ecommerce Consult"), 
    ("Website Design", "Website Design"),
    ("Website Updates", "Website Updates"),
    ("Integrations", "Integrations"),
    ("Other", "Other"),  
]

INTERNAL_PROGRESS = [
    ("RECEIVED", "RECEIVED"),
    ("AKNOWLEDGED", "AKNOWLEDGED"),
    ("CONTACTED", "CONTACTED"),
    ("IN PROGRESS","IN PROGRESS"),
    ("IN REVIEW", "IN REVIEW"),
    ("DONE", "DONE"),
]

def customer_id_gen():    
        random_int = str(get_random_string(8).upper())
        while Customer_contact_info.objects.filter(customer_id=random_int).exists():       
            random_int = int(get_random_string(8))    
        return random_int

# Create your models here.

class Customer_contact_info(models.Model):
    customer_id = models.CharField(primary_key=True, default=customer_id_gen, max_length=16, editable=False, unique=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_email = models.EmailField(max_length=255)
    customer_phone = PhoneNumberField(max_length=15, blank=True)
    customer_contact_subject = models.CharField(max_length=50, blank=True, null=True)
    internal_customer_contact_subject = models.CharField(max_length=30, choices=CONTACT_SUBJECT_CHOICES, blank=True, null=True)
    customer_notes = models.TextField(help_text='Why ya wanna reach out here?')
    internal_progress = models.CharField(max_length=20, choices=INTERNAL_PROGRESS, blank=True, null=True)
    work_estimate = models.FloatField(null=True, blank=True)
    payment_complete = models.BooleanField(default=False, editable=True)
    submission_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = "Customer Contact"
        verbose_name_plural = "Customers"

    def __str__(self) -> str:
        return self.customer_name
    

    



  
