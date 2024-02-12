from django.forms import ModelForm
from processes.models import processes


# Create the form class.
class ProcessForm(ModelForm):
    class Meta:
        model = processes
        fields = '__all__'