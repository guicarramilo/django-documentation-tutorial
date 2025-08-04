'''This is where we store views (no grosso, as telas).
    For them to be accessed, they need to be mapped to an url.
    This is done in the urls.py file on the app directory (djangotutorial/polls/urls.py)
'''

from django.http import HttpResponse

'''This is not on the documentation yet, but i figure the index
 is the one shown first, same as html index files'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")