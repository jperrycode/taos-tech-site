from django.contrib import admin
from .models import DjServices

# Register your models here.
@admin.register(DjServices)
class DjServiceAdmin(admin.ModelAdmin):
    list_display = (
        'dj_service_name', 'dj_service_description', 'dj_fully_booked'
    )