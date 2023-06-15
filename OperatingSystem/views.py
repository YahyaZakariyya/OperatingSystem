from django.shortcuts import render
# from django.http import HttpResponseRedirect
from processes.models import processes
from math import ceil

def home(request):
    data = {
        "title":"Operating Systems",
    }
    return render(request, 'index.html', data)

def dispatchProcess(request):
    data = {
        "title":"Dispatch Process",
    }
    return render(request, "dispatchProcess.html",data)

def processManagement(request):
    data = {
        "title":"Process Management",
    }
    return render(request, "processManagement.html",data)


def process(request):
    process_table = processes.objects.all()
    data = {
        "title":"Process",
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
        "schedualing":"First Come First Serve(FCFS)",
        "process_table":dictonary,
        "gantt_chart":gantt_chart,
        # "process_states":process_states,
        "counter":range(count),
    }

    return render(request, "schedualing.html", data)

def priority(request):
    process_table = processes.objects.all().order_by('priority')
    count = 0
    process = list()
    pcb = list()

    for i in process_table:
        process.append(i)

    while process:
        flag = True
        for i in process:
            print(i.process_id, i.priority)
            if i.arrival_time <= count:
                print("IF break")
                pcb.append(i)
                process.remove(i)
                flag = False
                count+=i.burst_time
                break
        if flag:
            count+=1

    dictonary = {}
    count = 0
    gantt_chart = []
    for i in pcb:
        gantt_chart.append(count)
        if count < i.arrival_time:
            gantt_chart.append('idle')
            count += i.arrival_time-count
            gantt_chart.append(count)
        gantt_chart.append(i.process_id)
        dictonary[i.process_id] = {}
        dictonary[i.process_id]["PID"] = i.process_id
        dictonary[i.process_id]["Priority"] = i.priority
        dictonary[i.process_id]["Arrival Time"] = i.arrival_time
        dictonary[i.process_id]["Burst Time"] = i.burst_time
        dictonary[i.process_id]["Response Time"] = count - i.arrival_time
        count+=i.burst_time
        dictonary[i.process_id]["Turnaround Time"] = count - i.arrival_time
        dictonary[i.process_id]["Waiting Time"] = dictonary[i.process_id]["Turnaround Time"] - i.burst_time
    gantt_chart.append(count)

    data = {
        "title":"Process Management",
        "schedualing":"Priority(Non-Preemptive)",
        "process_table":dictonary,
        "gantt_chart":gantt_chart,
        # "process_states":process_states,
        "counter":range(count),
    }

    return render(request, "schedualing.html", data)
    

def memoryManagement(request):
    memorySize = 1024
    frameSize = 4
    usedMemory = 0
    process_table = processes.objects.all()
    dictonary = {}
    for i in process_table:
        if usedMemory + ceil(i.memory/frameSize) > memorySize:
            continue
        usedMemory += ceil(i.memory/frameSize)
        dictonary[i.process_id] = ceil(i.memory/frameSize)
    usedMemory*=frameSize
    freeMemory = memorySize-usedMemory
    data = {
        "title":"Memory Management",
        "page_size":dictonary,
        "total_space":memorySize,
        "total_prcnt":int(memorySize/memorySize)*100,
        "used_space":usedMemory,
        "used_prcnt":int((usedMemory/memorySize)*100),
        "free_space":freeMemory,
        "free_prcnt":int((freeMemory/memorySize)*100),
    }
    print(int((usedMemory/memorySize)*100))
    return render(request, "memoryManagement.html", data)

def lru_page_replacement(request):
    page_string = "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1"
    pages = [int(page) for page in page_string.split(",")]
    frame_size = 4
    frames = []
    page_faults = 0
    lru = list()

    for page in pages:
        if page in frames:
            frames.remove(page)
            frames.append(page)
        else:
            page_faults += 1
            if len(frames) == frame_size:
                frames.pop(0)
            frames.append(page)
        lru.append(frames)

    data = {
        "title":"LRU Management",
    }
    return render(request, "memoryManagement.html", data)
