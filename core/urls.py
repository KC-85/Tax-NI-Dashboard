from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('', include('dashboard.urls')),  # Include dashboard app URLs
]

handler400 = "dashboard.views.error_400"
handler403 = "dashboard.views.error_403"
handler404 = "dashboard.views.error_404"
handler500 = "dashboard.views.error_500"

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
