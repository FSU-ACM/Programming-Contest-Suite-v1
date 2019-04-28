from django import forms
from django.core import validators
from registration.models import Team

class TeamForm(forms.Form):
    TeamName = forms.CharField(
        label='Team Name',
        widget=forms.TextInput(attrs={'placeholder': 'Team Name'})
    )
    
    Division = forms.ChoiceField(widget=forms.RadioSelect(), choices=Team.DIVISION, required=True)
        
    def reclean(self, fields):
        teamErrors = {}
        if not validTeamName(fields):
            teamErrors['TeamName'] = 'This name is already taken'

        if not teamErrors:
            return True
        else:
            self.add_error(None, teamErrors)
            return False
