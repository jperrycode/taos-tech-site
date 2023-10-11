from django.urls import path
from . import views
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('ecommerce/', EcomPageView.as_view(), name='ecom'),
    path('webservices/', WebPageView.as_view(), name='web'),
    path('contact_us/success/', SuccessPageView.as_view(), name='contact_suc'),
    path('webservices/fail-to-send/', FailPageView.as_view(), name='contact_fail'),
]