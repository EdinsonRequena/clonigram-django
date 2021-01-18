"""
User forms.
"""
# Internal Django Modules
from django import forms
from django.contrib.auth.models import User
# Users Modules
from users.models import Profile

class SingupForm(forms.Form):
    """Sing Up Form.
    """

    username = forms.CharField(min_length=4, max_length=20)

    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())


    def clean_username(self):
        """Username must be unique.
        """

        username = self.cleaned_data['username']
        q = User.objects.filter(username=username).exists()
        if q:
            raise forms.ValidationError('Username is already exists')

        return username


    def clean(self):
        """Verify password confitmation match.
        """

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError("Passwords don't match.")

        return data


    def save(self):
        """Create user and profile.
        """
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForms(forms.Form):
    """Profile form.
    """

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()