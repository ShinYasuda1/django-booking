from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
