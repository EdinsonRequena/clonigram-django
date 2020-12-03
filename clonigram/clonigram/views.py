'''Clonigram views'''

# Django modules
from django.http import HttpResponse
import json


# Utilities
from datetime import datetime as dt

def hello_world(request):
    ''' Return a Gretting'''
    hour = dt.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse(f'Hello, the server time is: {hour}')


def hi(request):
    """HI"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sort_int = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sort_int,
        'msg': 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
        )