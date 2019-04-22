from django import forms
from django.core.exceptions import ValidationError
from bcrypt import hashpw, gensalt
from registration.utility.auth import *
from registration.models import Account, Team

class QuickForm(forms.Form):
    TeamName = forms.CharField(
        label='Team Name',
        widget=forms.TextInput(attrs={'placeholder': 'Team Name'})
    )
    
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

    Division = forms.ChoiceField(widget=forms.RadioSelect(), choices=Team.DIVISION, required=True)
    Role = forms.ChoiceField(widget=forms.RadioSelect(), choices=Account.ROLE, required=True)
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    Password = forms.CharField(widget=forms.PasswordInput())
        
    def finalize(self, req):
        if not userExists(req.POST):
            newUser = Account(
                FirstName=req['FirstName'],
                LastName=req['LastName'],
                FsuID=req['FsuID'],
                FsuNum=req['FsuNum'],
                Email=req['Email'],
                Password=hashpw(req['Password'], gensalt()),
            )
            newUser.save(commit=False)

            newTeam = Team(
                TeamName=req['TeamName'],
                Division=req['Division'],
                Leader_id=newUser.AccountID
            )
            newTeam.save(commit=False)

            newUser.Team_id = newTeam.TeamID
            newUser.save()
            newTeam.save()
    
    