from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from registration.forms.quick import QuickForm

def dispatch(req):
    if req.method == 'GET':
        return home(req)
    else:
        return submit(req)

def home(req):
    form = QuickForm()
    return TemplateResponse(req, 'register.html', {'form': form})

def submit(req):
    form = QuickForm(req.POST)
    """
    if not form.is_valid():
        return TemplateResponse(req, 'register.html', {'form': form})
    else:
    """
    form.save(req.POST)
    return TemplateResponse(req, 'base.html', {})