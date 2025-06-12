from django.urls import path

from . import views
from .views import *




urlpatterns = [

    path('taos-haus-thumps/', DjPageView.as_view(), name='this-justin'),
    path('oops-only-bangers-radio/', DjRadioView.as_view(), name='radio'),
    path('taos-haus-review/', DjReviewView.as_view(), name='review-dj'),
    path('leave-review/submit/', ReviewPost.as_view(), name='review_us_post'),
    path("section/about-dj/", views.dj_about_section, name="dj_about_section")

]
