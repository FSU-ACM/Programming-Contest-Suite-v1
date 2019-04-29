"""
Registration App Views
- assess and handle requests based on source of request
  and content of its data
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from registration.utility.auth import getUser
from registration.utility.register import addAccount, addTeam
from registration.forms.solo import SoloForm
from registration.forms.team import TeamForm
from registration.forms.login import LoginForm
from registration.models import Account, Team, Course
from registration.utility.resources import ExportCSV
from registration.utility.fields import *

def register(req):
    """
    - handle requests from /register
    - POST:
        * bind form data
        * validate form data
        * render login page upon successful registration,
          raise error otherwise
    - GET:
        * render blank quick register form
    """
    SoloFormSet = formset_factory(SoloForm, extra=3, max_num=3)
    if req.method == 'POST':
        soloForms = SoloFormSet(req.POST)
        teamForm = TeamForm(req.POST)
        valid = True
        if not teamForm.is_valid() or not teamForm.reclean(
                teamForm.cleaned_data):
            valid = False
        if soloForms.is_valid():
            info = soloForms.cleaned_data
            for i, form in enumerate(soloForms):
                if form.is_valid() and info[i]:
                    if not form.reclean(info[i]):
                        valid = False
        else:
            valid = False

        if valid:
            teamInfo = teamForm.cleaned_data
            userInfo1 = info[0]
            userInfo2 = info[1]
            userInfo3 = info[2]
            user1 = addAccount(userInfo1)
            members = list(user1.__str__())
            memID = list(user1.AccountID)

            if userInfo2:
                user2 = addAccount(userInfo2)
                members.append(user2.__str__())
                memID.append(user2.AccountID)
                numMembers=2

            if userInfo3:
                user3 = addAccount(userInfo3)
                members.append(user3.__str__())
                memID.append(user3.AccountID)
                numMembers=3

            memInfo = zip(memID, members)
            team = addTeam(teamInfo, user1.AccountID, memInfo, numMembers)
            user1.Team_id = team.TeamID
            user1.save()

            if userInfo2:
                user2.Team_id = team.TeamID
                user2.save()
            if userInfo3:
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


def delete(req):
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

    if req.method == 'POST':
        if user.AccountID == team.Leader_id and team.Count > 1:
            if team.Count == 2:
                leader, member1 = team.MemberIDs.split(',')
                team.memberIDs = ''
                team.memberIDs = member1
                team.Count -= 1
                team.Leader_id = member1
                Account.objects.filter(AccountID=req.session['a_id']).delete()
            else:
                leader, member1, member2 = team.MemberIDs.split(',')
                team.memberIDs = ''
                team.memberIDs = str(member1)+str(',')+str(member2)
                team.Count -= 1
                team.Leader_id = member1
                Account.objects.filter(AccountID=req.session['a_id']).delete()
            team.save()

        elif user.AccountID == team.Leader_id and team.Count == 1:
            Account.objects.filter(AccountID=req.session['a_id']).delete()
            Team.objects.filter(TeamID=user.Team_id).delete()

        elif user.AccountID != team.Leader_id and team.Count > 1:
            if team.Count ==2:
                leader, member1 = team.MemberIDs.split(',')
                team.memberIDs = ''
                team.memberIDs = leader
                #team.Count -= 1
                #team.save()
            else:
                leader, member1, member2 = team.MemberIDs.split(',')
                team.memberIDs = ''
                if user.accountID == member1:
                    team.memberIDs = str(leader)+str(',')+str(member2)
                elif user.AccountID == member2:
                    team.memberIDs = str(leader)+str(',')+str(member1)

            Account.objects.filter(AccountID=req.session['a_id']).delete()
            team.Count -= 1
            team.save()
        else:
            Account.objects.filter(AccountID=req.session['a_id']).delete()

        try:
            del req.session['a_id']
        except KeyError:
            pass
        return HttpResponseRedirect('/')

    else:
        pass
    return render(req, 'delete.html', {'userInfo': userInfo})


def teamtsv(req):
    """
    Creates teams.tsv on server drive for use with DomJudge.
    """
    if req.method == 'GET':
        ExportCSV("Team")
        return HttpResponseRedirect('/createtsv')


def accountstsv(req):
    """
    Creates accounts.tsv on server drive.
    """
    if req.method == 'GET':
        ExportCSV("Accounts")
    return HttpResponseRedirect('/createtsv')
