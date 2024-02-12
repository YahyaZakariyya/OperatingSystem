"""
URL configuration for OperatingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from processes.views import ProcessViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'processes', ProcessViewSet)


urlpatterns = [
    path('api/',include(router.urls)),
    path('admin/', admin.site.urls, name='admin'),
    path('', TemplateView.as_view(template_name='home/index.html')),
    path('process-management/', include("processes.urls"))
    # path('memoryManagement/',views.memoryManagement,name="memoryManagement"),
    # path('memoryManagement/paging/',views.noofpages,name="paging"),
    # path('memoryManagement/lru/',views.lru_page_replacement,name="lru"),
]
