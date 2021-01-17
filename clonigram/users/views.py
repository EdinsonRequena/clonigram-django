"""
Users Views
"""
# Internal Django Modules
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
# Users Modules
from users.models import Profile
from users.forms import ProfileForms

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForms(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data('website')
            profile.website = data('phone_number')
            profile.website = data('biography')
            profile.website = data('picture')
            profile.save()

            return redirect('update_profile')
        else:
            form = ProfileForms()
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': Profile,
            'user': request.user,
        }
    )


def login_view(request):
    """Login view.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    
    return render(request, 'users/login.html')


def signup(request):
    """Sign up view.
    """
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirm = request.POST['passwd_confirm']

        if passwd != passwd_confirm:
            return render(request, 'users/signup.html', {'error': "Password and Password confirmation doesn't match"})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': "Username alredy exists"})

        user.firts_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')




@login_required
def logout_view(request):
    """Logout a user
    """
    logout(request)
    return redirect('login')
