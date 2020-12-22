"""
    Users Views
"""

# Django dependecies
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def login_view(request):
    """Login view.
    """
    return render(request, 'users/login.html')
