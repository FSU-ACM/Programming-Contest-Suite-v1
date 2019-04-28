from django.shortcuts import render
from checkin.forms.emailCheckin import emailCheckinForm
from checkin.forms.swipeCheckin import swipeCheckinForm
from django.core.mail import EmailMessage
from registration.models import Account
from registration.models import Team

# method to send DOMJudge login credentials
def sendEmail(user):
    mail_subject = 'Your DOMJudge Credentials'
    message = 'This is a test message.'
    to_email = user.Email
    email = EmailMessage(
                mail_subject, message, to=[to_email]
    )
    email.send()

def emailCheckin(req):
    if req.method == 'POST':
        form = emailCheckinForm(req.POST)
        if form.is_valid() and form.validUser(req):
            User = Account.objects.get(Email=req['Email'])
            sendEmail(User)
            return render(req, 'checkinSuccess.html')
    else:
        form = emailCheckinForm()

    return render(req, 'emailCheckin.html', {'form': form})

def swipeCheckin(req):
    if req.method == 'POST':
        form = swipeCheckinForm(req.POST)
        if form.is_valid() and form.validUser(req):
            User = Account.objects.get(FsuNum=form.parse())
            sendEmail(User)
            return render(req, 'checkinSuccess.html')
    else:
        form = swipeCheckinForm()

    return render(req, 'swipeCheckin.html', {'form': form})
