from django.shortcuts import render
from checkin.forms.checkin import CheckinForm

def checkin(req):
    if req.method == 'POST':
        form = CheckinForm(req.POST)
        if form.is_valid():
            form.finalize(req.POST)
            return render(req, 'base.html')
    else:
        form = CheckinForm()

    return render(req, 'checkin.html', {'form': form})
