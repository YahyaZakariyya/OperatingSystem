from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    data = {
        "title":"Operating Systems",
    }
    return render(request, 'index.html', data)

def process(request):
    data = {
        "title":"Process Management",
        "processes":[
            {"pid":1,"at":0,"bt":4},
            {"pid":2,"at":2,"bt":3},
            {"pid":3,"at":5,"bt":7}
        ]
    }
    return render(request, "process.html",data)

def process_form(request):
    try:
        pid = request.GET['pid']
        at = request.GET['at']
        bt = request.GET['bt']
        button = request.GET['create']
        return HttpResponseRedirect('/process/')
        print('try block')
    except:
        print('except block')
        pass
    return render(request, 'processform.html')

def create_process(request):
    try:
        pid = request.GET['pid']
        at = request.GET['at']
        bt = request.GET['bt']
    except:
        pass
    return render(request, 'process.html')