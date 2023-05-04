# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

# def process(request):
#     return HttpResponse("This is process button")