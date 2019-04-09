from django.template.response import TemplateResponse

def dispatch(req):
    return TemplateResponse(req, 'register.html', {})
