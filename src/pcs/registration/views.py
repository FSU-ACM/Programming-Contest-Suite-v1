"""
Registration App Views
- assess and handle requests based on source of request and content of its data 
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import formset_factory
from registration.utility.auth import getUser
from registration.utility.register import addAccount, addTeam
from registration.forms.solo import SoloForm
from registration.forms.team import TeamForm
from registration.forms.login import LoginForm
from registration.models import Account, Team, Course
from registration.utility.resources import ExportCSV


def register(req):
    """
    - handle requests from /register
    - POST:
        * bind form data
        * validate form data
        * render login page upon successful registration, raise error otherwise
    - GET:
        * render blank quick register form 
    """
    SoloFormSet = formset_factory(SoloForm, extra=3, max_num=3, validate_min=1, validate_max=3)
    if req.method == 'POST':
        soloForms = SoloFormSet(req.POST)
        teamForm = TeamForm(req.POST)
        if soloForms.is_valid() and teamForm.is_valid() and teamForm.reclean(teamForm.cleaned_data):
            info = soloForms.cleaned_data
            valid = True
            for i, form in enumerate(soloForms):
                if form.is_valid() and info[i]:
                    if not form.reclean(info[i]):
                        valid = False

        if valid:
            teamInfo = teamForm.cleaned_data
            userInfo1 = info[0]
            userInfo2 = info[1]
            userInfo3 = info[2]
            members = {'1': userInfo1.__str__()}
            user1 = addAccount(userInfo1)

            if userInfo2:
                members['2'] = userInfo2.__str__()
                user2 = addAccount(userInfo2)
            if userInfo3:
                members['3'] = userInfo3.__str__()
                user3 = addAccount(userInfo3)

            team = addTeam(teamInfo, user1.AccountID, members)
            user1.Team_id = team.TeamID
            user1.save()

            if user2 is not None:
                user2.Team_id = team.TeamID
                user2.save()
            if user3 is not None:
                user3.Team_id = team.TeamID
                user3.save()

            return HttpResponseRedirect('/login')

    else:
        soloForms = SoloFormSet()
        teamForm = TeamForm()

    return render(req, 'forms/quick.html', {'teamForm': teamForm, 'soloForms': soloForms})


def login(req):
    """
    - handle requests from /login
    - POST:
        * bind form data
        * validate form data
        * authenticate user
        * create session for user; attach account ID
        * render profile page upon successful login, raise error otherwise
    - GET: 
        * render blank login form
    """
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid() and form.validUser(req.POST):
            user = getUser(req.POST)
            req.session.set_expiry(0)
            req.session['a_id'] = user.AccountID
            return HttpResponseRedirect('/profile/options')
    else:
        form = LoginForm()

    return render(req, 'login.html', {'form': form})


def logout(req):
    """
    - delete session for user
    - redirect to homepage
    """
    try:
        del req.session['a_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/')


def profile(req):
    """
    if req.method == 'POST':
        form = ProfileForm(req.POST)
    else:
        form = ProfileForm()
    """
    user = Account.objects.get(AccountID=req.session['a_id'])
    team = Team.objects.get(TeamID=user.Team_id)
    course = Course.objects.filter(account=user.AccountID)
    courses = {}
    courseList = list()
    for i in course:
        courses[i.CourseID] = i.CourseName
        courseList.append(i.CourseName)

    userInfo = {
        'FirstName': user.FirstName,
        'LastName': user.LastName,
        'Email': user.Email,
        'TeamName': team.TeamName,
        'Courses': courses,
        'CourseList': courseList
    }
    return render(req, 'profile.html', {'userInfo': userInfo})


def manage(req):
    user = Account.objects.get(AccountID=req.session['a_id'])
    team = Team.objects.get(TeamID=user.Team_id)
    course = Course.objects.filter(account=user.AccountID)
    courses = {}
    courseList = list()
    for i in course:
        courses[i.CourseID] = i.CourseName
        courseList.append(i.CourseName)

    userInfo = {
        'FirstName': user.FirstName,
        'LastName': user.LastName,
        'Email': user.Email,
        'TeamName': team.TeamName,
        'Courses': courses,
        'CourseList': courseList
    }
    return render(req, 'manage.html', {'userInfo': userInfo})


def courses(req):
    user = Account.objects.get(AccountID=req.session['a_id'])
    team = Team.objects.get(TeamID=user.Team_id)
    course = Course.objects.filter(account=user.AccountID)
    courses = {}
    courseList = list()
    for i in course:
        courses[i.CourseID] = i.CourseName
        courseList.append(i.CourseName)

    userInfo = {
        'FirstName': user.FirstName,
        'LastName': user.LastName,
        'Email': user.Email,
        'TeamName': team.TeamName,
        'Courses': courses,
        'CourseList': courseList
    }
    return render(req, 'courses.html', {'userInfo': userInfo})


def options(req):
    user = Account.objects.get(AccountID=req.session['a_id'])
    team = Team.objects.get(TeamID=user.Team_id)
    course = Course.objects.filter(account=user.AccountID)
    courses = {}
    courseList = list()
    for i in course:
        courses[i.CourseID] = i.CourseName
        courseList.append(i.CourseName)

    userInfo = {
        'FirstName': user.FirstName,
        'LastName': user.LastName,
        'Email': user.Email,
        'TeamName': team.TeamName,
        'Courses': courses,
        'CourseList': courseList
    }
    return render(req, 'options.html', {'userInfo': userInfo})


def teamcsv(req):
    """
    Creates teams.csv on server drive for use with DomJudge.
    """
    if req.method == 'GET':
        ExportCSV("Team")
        return HttpResponseRedirect('/createcsv')


def accountscsv(req):
    """
    Creates accounts.csv on server drive.
    """
    if req.method == 'GET':
        ExportCSV("Accounts")
    return HttpResponseRedirect('/createcsv')
