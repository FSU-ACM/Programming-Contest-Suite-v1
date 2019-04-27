"""
Registration App Views
- assess and handle requests based on source of request and content of its data 
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from registration.forms.quick import QuickForm
from registration.forms.login import LoginForm
from registration.utility.auth import getUser


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
    if req.method == 'POST':
        form = QuickForm(req.POST)
        if form.is_valid() and form.finalize(req.POST):
            return HttpResponseRedirect('/login')
    else:
        form = QuickForm()
    
    return render(req, 'forms/quick.html', {'form': form})


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
            return HttpResponseRedirect('/profile')
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
    return render(req, 'profile.html')

def manage(req):
    return render(req, 'manage.html')

def courses(req):
    return render(req, 'courses.html')

def options(req):
    return render(req, 'options.html')