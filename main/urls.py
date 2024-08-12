from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

admin.site.site_header = 'Taos Haus Tech'
admin.site.index_title = 'THTS Data'

urlpatterns = [
    path('', RedirectView.as_view(url='tech-solutions/')),
    path('admin/', admin.site.urls),
    path('tech-solutions/', include('frontend.urls')),
    path('dj/', include('djapp.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
