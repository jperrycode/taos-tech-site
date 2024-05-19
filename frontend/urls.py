from django.urls import path
from .views import *
from . import views 
from django.conf.urls.static import static 

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    # path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('contact-thts/', Contact_model_view.as_view(), name='contact_page'),
    path('ecommerce/', EcomPageView.as_view(), name='ecom'),
    path('webservices/', WebPageView.as_view(), name='web'),
    path('contact-us-success/', views.SuccessPageView, name='contact_suc'),
    path('contact-us-fail/', FailPageView.as_view(), name='contact_fail'),
    path('the-team/', TeamPageView.as_view(), name='team'),
    path('stage/', StagePageView.as_view(), name='stage'),

]