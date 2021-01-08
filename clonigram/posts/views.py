'''
Posts views
'''
# Django dependencies
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime as dt

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Andrea Viñas',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': dt.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Edinson Requena',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': dt.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': dt.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

@login_required
def list_posts(request):
    '''
    :type posts: List
    :rtype: List
    '''
    return render(request, 'posts/feed.html', {'posts': posts})

