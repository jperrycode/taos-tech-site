from django import forms
from django.core.validators import EmailValidator
from phonenumber_field.formfields import PhoneNumberField
from .models import Customer_contact_info 


# from django.conf import settings
# from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    class Meta:
        model = Customer_contact_info
        fields = ('customer_name', 'customer_email', 'customer_phone', 'customer_contact_subject', 'customer_notes')

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Name'}),
            'customer_email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Your Email'}),
            'customer_phone':forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Your Phone Number'}),
            'customer_contact_subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject'}),
            'customer_notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'What can I do for you?'}),
        }



