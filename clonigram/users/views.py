"""
Users Views
"""
# Internal Django Modules
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Users Modules
from users.forms import ProfileForms, SingupForm

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
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SingupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

@login_required
def logout_view(request):
    """Logout a user
    """
    logout(request)
    return redirect('login')
