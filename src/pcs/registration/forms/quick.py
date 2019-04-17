from django import forms
from django.core.exceptions import ValidationError
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

    def __init__(self, req=None):
        super().__init__()
        if req is not None:
            self.FirstName=req['FirstName']
            self.LastName=req['LastName']
            self.FsuID=req['FsuID']
            self.FsuNum=req['FsuNum']
            self.Email=req['Email']
            self.Password=req['Password']
            self.TeamName=req['TeamName']
            self.Division=req['Division']

    def validUser(self):
        if Account.objects.get(Email=self.Email) is not None:
            raise ValidationError(('User already exists'), code='exists')
        else:
            return True
        
    def finalize(self):
        if self.validUser():
            newUser = Account(
                FirstName=self.FirstName,
                LastName=self.LastName,
                Email=self.Email,
                FsuID=self.FsuID,
                FsuNum=self.FsuNum,
                Password=self.Password
            )
            newUser.save()
            newUser = Account.objects.get(Email=self.Email)

            newTeam = Team(
                TeamName=self.TeamName,
                Division=self.Division,
                Leader_id=newUser.AccountID
            )
            newTeam.save()

            newTeam = Team.objects.get(Leader_id=newUser.AccountID)
            newUser.Team_id = newTeam.TeamID
            newUser.save()

    
    