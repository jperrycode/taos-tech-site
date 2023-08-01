from django.urls import path
from . import views
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.mainpageview, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
]