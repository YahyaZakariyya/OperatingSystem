from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from processes.models import processes
from django.views import View
from django.urls import reverse_lazy
from processes.forms import ProcessForm
from rest_framework import viewsets
from processes.serializers import ProcessSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = processes.objects.all()
    serializer_class = ProcessSerializer

class ProcessCreate(LoginRequiredMixin, View):
    template = 'processes/process_form.html'
    success_url = reverse_lazy("processes:all")

    def get(self, request):
        form = ProcessForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = ProcessForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        form.save()
        form.clean
        return redirect(self.success_url)
    
class ProcessDelete(LoginRequiredMixin, View):
    model = processes
    success_url = reverse_lazy('processes:all')
    template = 'processes/process_confirm_delete.html'

    def get(self, request, pk):
        process = get_object_or_404(self.model, pk=pk)
        ctx = {'process': process}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        process = get_object_or_404(self.model, pk=pk)
        process.delete()
        return redirect(self.success_url)


def processSchedualing(request):
    data = {
        "title":"Dispatch Process",
    }
    return render(request, "processes/dispatchProcess.html",data)

def processManagement(request):
    process_table = processes.objects.all()
    data = {
        "title":"Process Management",
        "process_table":process_table
    }
    return render(request, "processes/processManagement.html",data)


def process(request):
    process_table = processes.objects.all()
    data = {
        "title":"Process",
        "process_table":process_table
    }
    return render(request, "processes/process.html",data)

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

    return render(request, "processes/schedualing.html", data)

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
            if i.arrival_time <= count:
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

    return render(request, "processes/schedualing.html", data)
