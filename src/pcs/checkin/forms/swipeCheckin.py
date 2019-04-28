# Checkin form to register their attendance at a contest

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from registration.models import Account
from registration.utility import auth

class swipeCheckinForm(forms.Form):
    fsuNum = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'FSU Number'}))

    # determines if the swipe is valid
    def validRead(self):
        if self.fsuNum[1] == 'B':
            return True
        return False

    # returns last 8 numbers of fsu number
    def parse(self):
        return self.fsuNum[10:18]

    def validUser(self, req):
        errors = {}
        if self.validRead():
            req['fsuNum'] = self.parse()
        # userExists will check that user is in db
        # if they don't match or are not in the db an error will
        # display and the user will have to try again.
        try:
            user = Account.objects.get(FsuNum=req['fsuNum'])
            user.isCheckedIn = True
            user.save()
            return True
        except ObjectDoesNotExist:
            errors['fsuNum'] = 'Check-in failed'
            self.add_error(None, errors)
            return False
