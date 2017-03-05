from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from .forms import loginform
def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        return HttpResponseRedirect('index.html')
    else:
        form = loginform()
    template=loader.get_template('login_page/index.html')
    context={
        'form' : form,
    }
    return HttpResponse(template.render(context, request))
def sub(request):
    template=loader.get_template('login_page/q.html')
    return HttpResponse(template.render(request));
