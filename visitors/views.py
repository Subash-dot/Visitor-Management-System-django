from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def newVisitor(request):
    template = loader.get_template('addnewvisitor.html')
    return HttpResponse(template.render())

def test(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())