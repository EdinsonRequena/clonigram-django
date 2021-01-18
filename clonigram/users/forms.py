"""
User forms.
"""
# Internal Django Modules
from django import forms

class SingupForm(form.Form):
    """Sing Up Form.
    """

    username = forms.CharField(min_length=4, max_length=20)

    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length=6, max_length=70, widget=forms.EmailInput())




class ProfileForms(forms.Form):
    """Profile form.
    """

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()