from django.shortcuts import render
from django.http import HttpResponse
import webbrowser

def index(request):
    output = "<form method='GET' action='getrepos/'>"
    output += "<label for='reps'>repositories(split met &#34;&#59;&#34;)</label>"
    output += "</br>"
    output += "<textarea rows='4' cols='50' id='reps' name='reps'>"
    output += "</textarea>"
    output += "</br>"
    output += "<input type='submit' name='submit' id='submit'></input>"
    output += "</form>"
    return HttpResponse(output)

def getrepos(request):
    repString = request.GET.get('reps')
    repArray = repString.split(';');
    output = ""
    for rep in repArray:
        url = constructDownloadURL(rep)
        webbrowser.open(url, new=2, autoraise=True)
        output += url
    return HttpResponse(output)

def constructDownloadURL(url):
    #https://github.com/user/repo/zipball/master
    #https://github.com/user/repo/archive/master.zip
    return (url + "/archive/master.zip")
    
