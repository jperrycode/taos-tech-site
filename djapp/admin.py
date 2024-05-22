from django.contrib import admin
from .models import DjServices, Reviews

# Register your models here.
@admin.register(Reviews)
class DjServiceAdmin(admin.ModelAdmin):
    list_display = (
        'dj_service_name', 'dj_service_description', 'dj_fully_booked'
    )

    @admin.register(Reviews)
    class ReviewAdmin(admin.ModelAdmin):
        list_display = (
            'dj_service_name', 'dj_service_description', 'dj_fully_booked'
        )