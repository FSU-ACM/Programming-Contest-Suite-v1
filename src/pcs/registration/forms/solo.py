from django import forms
from django.core.exceptions import ValidationError
from bcrypt import hashpw, gensalt
from registration.utility.auth import userExists
from registration.utility.validators import *
from registration.models import Account

class SoloForm(forms.Form):
    FirstName = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    
    LastName = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    
    FsuID = forms.CharField(
        label='FSU ID',
        widget=forms.TextInput(attrs={'placeholder': 'abc19'})
    )

    FsuNum = forms.CharField(
        max_length=8,
        min_length=8,
        label='FSU Number',
        widget=forms.TextInput(attrs={'placeholder': 'Last 8 Digits of myFSU Card'})
    )

    Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    Password = forms.CharField(widget=forms.PasswordInput())
        
    Role = forms.ChoiceField(widget=forms.RadioSelect(), choices=Account.ROLE, required=False)
    
    def reclean(self, fields):
        soloErrors = {}
    
        if not validFSUID(fields):
            soloErrors['FsuID'] = 'FSU ID already linked to an account'
        
        if not validFSUNum(fields):
            soloErrors['FsuNum'] = 'Student number must only include numbers'
        elif not availableFSUNum(fields):
            soloErrors['FsuNum'] = 'Student number already linked to an account'

        if userExists(fields):
            soloErrors['Email'] = 'Email already linked to an account'

        if not soloErrors:
            return True
        else:
            self.add_error(None, soloErrors)
            return False
