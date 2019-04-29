from django.shortcuts import render
from checkin.forms.emailCheckin import emailCheckinForm
from checkin.forms.swipeCheckin import swipeCheckinForm
from django.core.mail import EmailMessage
from registration.models import Account
from registration.models import Team

# method to send DOMJudge login credentials

def sendEmail(User):
    contestAddress = 'domjudge.cs.fsu.edu'
    team = Team.objects.get(TeamID=User.Team)
    mail_subject = 'Your DOMJudge Credentials'
    message = User.FirstName + str(',\n')+str('\tYou are checked-in to the contest!')+str(' To log into DOMJudge, go to ') + str(contestAddress) +str(' and enter the credentials below. Thanks for participating!\n\n')+str('Username: ') + str(Team.TeamName) + str('\n') +str('Password: ') + str(Team.Password)
    to_email = user.Email
    email = EmailMessage(
                mail_subject, message, to=[to_email]
    )
    email.send()

# view to handle email check-in
# if the user entry is valid and the user exists in the DB
# then user will receive a confirmation email and success page displays
# if not in DB user is presented with the same form for reentry
def emailCheckin(req):
    if req.method == 'POST':
        form = emailCheckinForm(req.POST)
        if form.is_valid() and form.validUser(req.POST):
            User = Account.objects.get(Email=req.POST['Email'])
            sendEmail(User)
            return render(req, 'checkinSuccess.html')
    else:
        form = emailCheckinForm()

    return render(req, 'emailCheckin.html', {'form': form})

# view to handle swipe check-in
# if the user entry is valid and the user exists in the DB
# then user will receive a confirmation email and success page displays
def swipeCheckin(req):
    if req.method == 'POST':
        form = swipeCheckinForm(req.POST)
        if form.is_valid() and form.validUser(req.POST.copy()):
            User = Account.objects.get(FsuNum=form.parse(req.POST))
            sendEmail(User)
            return render(req, 'checkinSuccess.html')
    else:
        form = swipeCheckinForm()

    return render(req, 'swipeCheckin.html', {'form': form})
