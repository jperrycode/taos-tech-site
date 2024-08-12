from django.urls import path
from .views import *



urlpatterns = [

    path('taos-haus-thumps/', DjPageView.as_view(), name='this-justin'),
    path('taos-haus-review/', DjReviewView.as_view(), name='review-dj'),
    path('leave-review/submit/', ReviewPost.as_view(), name='review_us_post'),

]
