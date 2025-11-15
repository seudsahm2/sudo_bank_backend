from django.conf import settings
from django.contrib import admin
from django.urls import path
from core_apps.user_auth.views import TestLogging
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("",TestLogging.as_view(),name="test-logging"),
]
