# placeholder for crispyforms

# profile info will go here

# birb

# Login form to validate user input and log them into the system
from django import forms
from django.core.exceptions import ValidationError
from bcrypt import hashpw, gensalt

