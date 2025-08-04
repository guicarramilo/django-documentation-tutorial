from django.urls import path

'''imports all views from polls/views.py'''
from . import views

urlpatterns = [
    #This is not on the documentation yet, but i figure
    #the index is the one shown first, same as html index files
    #so views.index decides that it opens first
    path("", views.index, name="index"),
]

''' The next step is to configure the root URLconf 
in the mysite project to include the URLconf defined in polls.urls.'''