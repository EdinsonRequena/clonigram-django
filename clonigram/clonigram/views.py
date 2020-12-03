'''Clonigram views'''

# Django modules
from django.http import HttpResponse
import json


# Utilities
from datetime import datetime as dt

def hello_world(request):
    '''
    :type: hour: str
    :rtype: str
    '''
    hour = dt.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse(f'Hello, the server time is: {hour}')


def sorted_intengers(request):
    """
    :type nums: List[str]
    :type sort_int: List[int]
    :type data: Dict[int]
    :rtype: Dict
    """
    nums = [int(i) for i in request.GET['numbers'].split(',')]
    sort_int = sorted(nums)
    data = {
        'status': 'ok',
        'numbers': sort_int,
        'msg': 'Integers sorted succesfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
        )


def say_hi(request, name, age):
    '''
    :type name: str
    :type age: int
    :type msg: str
    :rtype: str
    '''
    if age < 12:
        msg = f'Sorry {name}, you are not allowed here!'
    else:
        msg = f'Hello, {name} Welcome to the system!!!'

    return HttpResponse(msg)