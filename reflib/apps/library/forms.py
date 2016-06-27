import authtools
from django import forms
from reflib.apps.customuser.models import User


class UserCreateForm(authtools.forms.UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
