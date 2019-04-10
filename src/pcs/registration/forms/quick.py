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
