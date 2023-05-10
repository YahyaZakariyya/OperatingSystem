from django.shortcuts import render

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