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

def fcfs(request):
    process_table = processes.objects.all().order_by('arrival_time')
    dictonary = {}
    count = 0
    gantt_chart = []
    for i in process_table:
        gantt_chart.append(count)
        if count < i.arrival_time:
            gantt_chart.append('idle')
            count += i.arrival_time-count
            gantt_chart.append(count)
        gantt_chart.append(i.process_id)
        dictonary[i.process_id] = {}
        dictonary[i.process_id]["PID"] = i.process_id
        dictonary[i.process_id]["Arrival Time"] = i.arrival_time
        dictonary[i.process_id]["Burst Time"] = i.burst_time
        dictonary[i.process_id]["Response Time"] = count - i.arrival_time
        count+=i.burst_time
        dictonary[i.process_id]["Turnaround Time"] = count - i.arrival_time
        dictonary[i.process_id]["Waiting Time"] = dictonary[i.process_id]["Turnaround Time"] - i.burst_time
    gantt_chart.append(count)
   
    data = {
        "title":"Process Management",
        "process_table":dictonary,
        "gantt_chart":gantt_chart,
    }

    return render(request, "schedualing.html", data)

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