'''
Post application module.
'''
from django.apps import AppConfig


class PostsConfig(AppConfig):
    '''
    :type name: str
    type verbose_name: str
    '''
    name = 'posts'
    verbose_name = 'Posts'
