"""
Users Views
"""
# Internal Django Modules
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.models import User
# Posts modules
from posts.models import Post
# Users Modules
from users.forms import ProfileForms, SingupForm

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view
    """
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ Add user's posts to context.
        """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["posts"] = Post.objects.filetr(user=user).order_by('-created')
        return context



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

            url = reverse('user:details', kwargs={'username': request.user.username})
            return redirect(url)
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
            return redirect('posts:feed')
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
            return redirect('users:login')
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
    return redirect('users:login')
