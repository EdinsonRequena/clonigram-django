""" Forms at Posts
"""

# Django Modules
from django import fomrs

# Posts Modules
from posts.models import Post

class PostForm(forms.ModelForm):
    """Posts model form.
    """

    class Meta:
        """form settings
        """

        model = Post
        fields = ('user', 'profile', 'title', 'photo')