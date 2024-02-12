from django.shortcuts import render
# from django.http import HttpResponseRedirect
from processes.models import processes
from math import ceil

# def home(request):
#     data = {
#         "title":"Operating Systems",
#     }
#     return render(request, 'index.html', data)

def memoryManagement(request):
    data = {
        "title":"Memory Management",
    }
    return render(request, "memoryManagement.html",data)
    

def noofpages(request):
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
    return render(request, "noofpages.html", data)

def lru_page_replacement(request):
    page_string = "7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1"
    pages = [int(page) for page in page_string.split(",")]
    frame_size = 4
    frames = []
    page_faults = 0
    lru = list()

    for page in pages:
        temp = frames.copy()
        if page in frames:
            frames.remove(page)
            frames.append(page)
            temp.insert(0,'Hit')
        else:
            page_faults += 1
            if len(frames) == frame_size:
                frames.pop(0)
            frames.append(page)
            temp.insert(0,'Miss')
        lru.append(temp)

    lru.pop(0)
    data = {
        "title":"LRU Management",
        "lru":lru,
        "frames":[x for x in range(1,frame_size+1)]
    }
    return render(request, "lru.html", data)
