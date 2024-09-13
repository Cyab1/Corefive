"""
URL configuration for corefive project.

The `urlpatterns` list routes URLs to views. For more information please see:
This module defines the URL patterns for the corefive project,
including admin URLs and any app-specific URL patterns.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("band.urls")),
    path("user_auth/", include("user_auth.urls")),
    path("user_auth/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
