from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    # add email field to form
    email = forms.EmailField()

    # define class Meta, so we can query the User model and specify the fields we want in our form
    class Meta:
        # model that will be affected
        model = User
        # fields that will be shown on form and in what order
        fields = ['username', 'email', 'password1', 'password2']