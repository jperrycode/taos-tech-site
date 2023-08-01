from django import forms
from django.core.validators import EmailValidator
from phonenumber_field.formfields import PhoneNumberField
from .models import Customer_contact_info


# from django.conf import settings
# from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form_control', 'id':'name', 'type':'text','placeholder':'Your name', }), required=True, max_length=50)
    customer_email = forms.EmailField(validators=[EmailValidator()], required=True, max_length=50)
    customer_phone = PhoneNumberField()
    customer_contact_subject = forms.CharField(required=True, max_length=100)
    customer_notes = forms.CharField(widget=forms.Textarea, max_length=2000)

    class Meta:
        model = Customer_contact_info
        fields = ['customer_name', 'customer_email', 'customer_phone', 'customer_contact_subject', 'customer_notes']