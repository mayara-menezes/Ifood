from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
    context = {}
    
    html_template = loader.get_template('home/index.html')
    
    return HttpResponse(html_template.render(context, request))