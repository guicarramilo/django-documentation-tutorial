'''The URL declarations for this Django project;
a “table of contents” of your Django-powered site.'''

''' add an import for django.urls.include in mysite/urls.py 
and insert an include() in the urlpatterns list'''


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #The path() function expects at least two arguments: route("polls/") and view(include("polls.urls")).
    #The include() function allows referencing other URLconfs.
    
    # Whenever Django encounters include(), it chops off whatever part of 
    # the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]