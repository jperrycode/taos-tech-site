from django.urls import path
from .views import *



urlpatterns = [

    path('taos-haus-thumps/', DjPageView.as_view(), name='this-justin'),
]
