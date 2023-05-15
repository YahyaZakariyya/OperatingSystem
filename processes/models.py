from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class processes(models.Model):
    process_id = models.CharField(max_length=3, unique=True)
    arrival_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    burst_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    # arrival_time = models.IntegerField(max_length = 100)
    # burst_time = models.IntegerField(max_length = 100)