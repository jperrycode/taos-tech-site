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



class StarRatingIntegerChoices(models.IntegerChoices):
    ONE = 1, 'One Star'
    TWO = 2, 'Two Stars'
    THREE = 3, 'Three Stars'
    FOUR = 4, 'Four Stars'
    FIVE = 5, 'Five Stars'
class Reviews(models.Model):
    reviewer_name = models.CharField(verbose_name='Your Name', max_length=250, blank=True, null=True)
    date_of_review = models.DateField(auto_now_add=True)
    review_event_type = models.CharField(verbose_name='What Event?',max_length=20, blank=True, null=True)
    date_of_event = models.DateField(verbose_name='Date of Event',blank=True, null=True, auto_now_add=False, auto_now=False)
    event_city = models.CharField(verbose_name='Where?',max_length=250, blank=True, null=True)
    star_rating = models.PositiveSmallIntegerField(choices=StarRatingIntegerChoices.choices)
    review_pass = models.BooleanField(default=False)
    rating_message_front = models.TextField(verbose_name='How did we Do?',blank=True, null=True)
    rating_message_dj = models.TextField(verbose_name='Comment for the DJs eyes only', blank=True, null=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

        def __str__(self) -> str:
            return self.reviewer_name

