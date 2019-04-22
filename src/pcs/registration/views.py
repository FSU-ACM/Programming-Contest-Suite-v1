"""
Registration App Views
- assess and handle requests based on source of request and content of its data 
"""

from django.shortcuts import render
from django.http import HttpResponseRedirect
from registration.forms.quick import QuickForm
from registration.forms.login import LoginForm


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
        if form.is_valid():
            form.finalize(req.POST)
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
        * render profile page upon successful login, raise error otherwise
    - GET: 
        * render blank login form
    """
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid() and form.validUser(req.POST):
            return HttpResponseRedirect('/profile')
    else:
        form = LoginForm()

    return render(req, 'login.html', {'form': form})

