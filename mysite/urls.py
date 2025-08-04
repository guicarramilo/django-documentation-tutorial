'''The URL declarations for this Django project;
a “table of contents” of your Django-powered site.'''

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]