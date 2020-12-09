'''
Post Models.
'''

from django.db import models

class User(models.Model):
    '''
    :type email: EmailField
    :type password: CharField
    :type first_name: CharField
    :type last_name: CharField
    :type is_admin: BooleanField
    :type bio: CharField
    :type birthdate: DateField
    :type created: DateTimeField
    :type modified: DateTimeField
    '''

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)