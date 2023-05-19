from django.shortcuts import render
from django.http import HttpResponseRedirect
from processes.models import processes

def home(request):
    data = {
        "title":"Operating Systems",
    }
    return render(request, 'index.html', data)

def process(request):
    process_table = processes.objects.all()
    data = {
        "title":"Process Management",
        "process_table":process_table
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