# Swipe check-in form to register their attendance at a contest

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from registration.models import Account
from registration.utility import auth


class swipeCheckinForm(forms.Form):
    FsuNum = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'FSU Number'}),
        label='Please swipe your FSUCard'
    )

    # determines if the swipe is valid
    def validRead(self, req):
        if req['FsuNum'][1] == 'B':
            return True
        return False

    # returns last 8 numbers of fsu number
    def parse(self, req):
        return req['FsuNum'][10:18]

    def validUser(self, req):
        errors = {}
        if self.validRead(req):
            req['FsuNum'] = self.parse(req)
        # userExists will check that user is in db
        # if user is in DB they will be marked as checked-in
        # if they don't match or are not in the db an error will
        # display and the user will have to try again.
        try:
            user = Account.objects.get(FsuNum=req['FsuNum'])
            user.isCheckedIn = True
            user.save()
            return True
        except ObjectDoesNotExist:
            errors['FsuNum'] = 'Check-in failed'
            self.add_error(None, errors)
            return False
