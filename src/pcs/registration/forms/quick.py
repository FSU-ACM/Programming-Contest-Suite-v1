from django import forms
from registration.models import Account, Team

DIVISION = (
        ('L', 'Lower Division'),
        ('U', 'Upper Division')
    )

ROLE = (
    ('P', 'Participant'),
    ('Q', 'Question Writer'),
    ('V', 'Volunteer')
)

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
        label='FSU Number',
        widget=forms.TextInput(attrs={'placeholder': 'Last 8 Digits on myFSU Card'})
    )

    Division = forms.ChoiceField(choices=DIVISION)
    Role = forms.ChoiceField(choices=ROLE)
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    Password = forms.CharField(widget=forms.PasswordInput())

    def save(self, req):
        exist = Account.objects.filter(Email=req['Email'])
        if not exist:
            return
    
        user = Account(
            FirstName=req['FirstName'],
            LastName=req['LastName'],
            Email=req['Email'],
            FsuID=req['FsuID'],
            FsuNum=req['FsuNum'],
            Password=req['Password']
        )
        
        user.save()
        newUser = Account.objects.get(Email=user.Email)

        team = Team(
            TeamName=req['TeamName'],
            Division=req['Division'],
            Leader_id=newUser.AccountID
        )
        team.save()

        newTeam = Team.objects.get(Leader_id=newUser.AccountID)
        newUser.Team_id = newTeam.TeamID
        newUser.save()

    
    