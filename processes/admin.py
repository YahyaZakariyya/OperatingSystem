from django.contrib import admin
from processes.models import processes

class processAdmin(admin.ModelAdmin):
    PCB = ('Process ID', 'Arrival Time', 'Burst Time')

admin.site.register(processes, processAdmin)

# Register your models here.
