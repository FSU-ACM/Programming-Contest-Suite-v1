from django.shortcuts import render
from checkin.forms.emailCheckin import emailCheckinForm
from checkin.forms.swipeCheckin import swipeCheckinForm
from django.core.mail import EmailMessage
from registration.utility import auth

def emailCheckin(req):
    if req.method == 'POST':
        form = emailCheckinForm(req.POST)
        if form.is_valid() and form.validUser():
            #form.finalize(req.POST)
            user = auth.getUser(req.POST)
            sendEmail(user)
            return render(req, 'base.html')
    else:
        form = emailCheckinForm()

    return render(req, 'checkin.html', {'form': form})

def swipeCheckin(req):
    if req.method == 'POST':
        form = swipeCheckinForm(req.POST)
        if form.is_valid() and form.validUser():
            #form.finalize(req.POST)
            user = auth.getUser(req.POST)
            sendEmail(user)
            return render(req, 'base.html')
    else:
        form = swipeCheckinForm()

    return render(req, 'checkin.html', {'form': form})

def sendEmail(user):
    mail_subject = 'Your DOMJudge Credentials'
    message = 'This is a test message.'
    to_email = user.Email
    email = EmailMessage(
                mail_subject, message, to=[to_email]
    )
    email.send()
