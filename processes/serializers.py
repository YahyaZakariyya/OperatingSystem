from rest_framework import serializers
from processes.models import processes
from django.urls import reverse

# create serializers

class ProcessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = processes
        fields = '__all__'