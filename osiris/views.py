# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import os
import logging
import httplib2
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage
from django.shortcuts import render
import tempfile
from testproject import settings
from ed import decode, encode

CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '', 'client_secrets.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/plus.me',
    redirect_uri='http://localhost:8000/oauth2callback')

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        print request.POST
        print request.FILES['file']
        _,filepath = tempfile.mkstemp()
        with open(filepath, "w") as f:
            f.write(request.FILES['file'].read())
        outputdir = tempfile.mkdtemp()
        encode(filepath, "640x480",outputdir + "/output.mp4")
        print outputdir
        return HttpResponse('RANDOM URL')
            # Redirect to the document list after POST
    else:
        form = DocumentForm() # A empty, unbound form

def download(request):
    if request.method == 'POST':
        link = request.POST.get("linka")
        print request.POST
        pat = tempfile.mkdtemp()
        string = ('youtube-dl -o %s/current.mp4 "'+ str(link) + '"')%pat
        print string
        os.system(string)
        dest = os.path.join("/static/", tempfile.mkdtemp())
        decode(pat + "/current.mp4", "640x480", dest+"/outpud.mp3")
        print dest  + "/outpud.mp3" 
        return HttpResponse('<a href=' + dest + '/outpud.mp3>Download File</a>')

def index(request):



    return render(request, 'index.html', {})
def auth_return(request):
    # request.user.token = request.REQUEST.get("access_code")
    return HttpResponseRedirect("/")

def login(request):
    return redirect("https://accounts.google.com/o/oauth2/auth?client_id=262696032830-q699mhlbtu0sbcd3duo91upht0ht4ati.apps.googleusercontent.com&redirect_uri=http://www.osiris.com/oauth2callback&response_type=code&scope=https://www.googleapis.com/auth/youtube&access_type=offline")