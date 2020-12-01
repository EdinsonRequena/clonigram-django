'''Clonigram views'''

# Django modules
from django.http import HttpResponse

# Utilities
from datetime import datetime as dt

def hello_world(request):
    hour = dt.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello, the server time is: {hour}')


