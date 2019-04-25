# Login form to validate user input and log them into the system
from django import forms
from django.core.exceptions import ValidationError
from bcrypt import hashpw, gensalt
from registration.models import Account
from registration.utility.auth import checkPass, userExists


class LoginForm(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))

    Password = forms.CharField(widget=forms.PasswordInput())

    def validUser(self, req):
        # checkPass will check that user is in db and that the
        # password matches that user.
        # if they don't match or are not in the db an error will
        # display and the user will have to try again.
        if userExists(req) and checkPass(req):
            # log user in to system
            # dummy statement
            return True
        else:
            raise ValidationError(('User/Password are not correct'), code='notexits')
        

