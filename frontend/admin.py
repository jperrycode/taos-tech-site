from django.contrib import admin
from .models import Customer_contact_info

class CustomerDataAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "customer_name", "customer_email",)

admin.site.register(Customer_contact_info, CustomerDataAdmin)