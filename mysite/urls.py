from django.contrib import admin
from django.urls import path, include  # Added 'include'
from django.conf import settings  # Added 'settings'
from django.conf.urls.static import static  # Added 'static'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("weatherapp.urls"))  # This includes your 'weatherapp' URLs
]

if settings.DEBUG:  # Serve media files during development only
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
