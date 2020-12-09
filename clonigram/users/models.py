'''
Users Models
'''

# Django dependencies
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Mode):
    '''
    Profile model

    Proxy model that extends the base data with other information
    '''

    