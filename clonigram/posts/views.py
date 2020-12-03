'''
Posts views
'''

from django.http import HttpResponse

# Utilities
from datetime import datetime as dt

posts = [
    {
        'name': 'My Dog.',
        'user': 'Andrea Viñas',
        'timestamp': dt.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'In San Francisco.',
        'user': 'Edinson Requena',
        'timestamp': dt.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': dt.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/784/200/200'
    },

]

def list_posts(request):
    '''
    :type content: List
    :type post: Dict{List}
    :rtype: List
    '''
    content = []
    
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i> </small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))

