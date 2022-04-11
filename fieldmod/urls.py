"""fieldmod URL Configuration"""

from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from tanksbase.views import main_view, TankView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


router = SimpleRouter()

router.register('api/tanksbase', TankView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="Field Modernization"),
    ]

urlpatterns += router.urls
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # added for AS3 settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
