from django.urls import path
from processes import views


app_name = 'processes'

urlpatterns = [
    path('',views.processManagement,name="all"),
    path('processSchedualing/',views.processSchedualing,name="processSchedualing"),
    path('processSchedualing/fcfs/',views.fcfs,name="fcfs"),
    path('processSchedualing/priority/',views.priority,name="priority"),
    path('create/', views.ProcessCreate.as_view(), name='process_create'),
    path('<int:pk>/delete/', views.ProcessDelete.as_view(), name="process_delete")
]