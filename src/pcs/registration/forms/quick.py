from django import forms

DIVISION = (
    ('L', 'Lower Division'),
    ('U', 'Upper Division')
)

ROLE = (
    ('P', 'Participant'),
    ('Q', 'Qeustion Writer'),
    ('V', 'Volunteer')
)


class QuickForm(forms.Form):
    TeamName = forms.CharField(
        label='Team Name',
        widget=froms.TextInput(attrs={'placeholder': 'Team Name'})
    )

    FirstName = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )

    LastName = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
