from django.contrib import admin
from .models import DjServices, Reviews

# Register your models here.
@admin.register(DjServices)
class DjServiceAdmin(admin.ModelAdmin):
    list_display = (
        'dj_service_name', 'dj_service_description', 'dj_fully_booked'
    )

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'reviewer_name', 'date_of_review', 'review_event_type', 'date_of_event', 'event_city','star_rating'
    )

