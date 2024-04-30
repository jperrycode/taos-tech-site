from django.contrib import admin
from .models import Customer_contact_info, EmployeeProfile, DjServices

class CustomerDataAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "customer_name", "customer_email", "submission_time")

admin.site.register(Customer_contact_info, CustomerDataAdmin)

@admin.register(EmployeeProfile)
class EmployeeForm(admin.ModelAdmin):
    list_display = (
        'emp_name', 'emp_specialties_1', 'emp_specialties_2', 'emp_specialties_3', 'emp_bio', 'active_employee')

@admin.register(DjServices)
class DjServiceAdmin(admin.ModelAdmin):
    list_display = (
        'dj_service_name', 'dj_service_description', 'dj_fully_booked'
    )