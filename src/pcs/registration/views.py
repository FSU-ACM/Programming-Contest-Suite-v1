from django.shortcuts import render
from registration.forms.quick import QuickForm

def dispatch(req):
    if req.method == 'POST':
        form = QuickForm(req.POST)
        if form.is_valid():
            form.finalize(req.POST)
            return render(req, 'base.html')
    else:
        form = QuickForm()
    
    return render(req, 'forms/quick.html', {'form': form})