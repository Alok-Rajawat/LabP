from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        return HttpResponseRedirect('registration_page/index.html')
    else:
        form = loginform()
    template=loader.get_template('registration_page/index.html')
    context={
        'form' : form,
    }
    template=loader.get_template('registration_page/index.html')
    return HttpResponse(template.render(request))
