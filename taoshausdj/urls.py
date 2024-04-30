from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPageView.as_view(), name='dj-home'),

]