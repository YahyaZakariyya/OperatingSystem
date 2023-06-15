from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models

input_regex = RegexValidator(
    regex=r'^P[0-9]{2}$',
    message="Input must start with 'P' followed by two integers letters."
)

# Create your models here.
class processes(models.Model):
    process_id = models.CharField(max_length=3, unique=True,validators=[input_regex])
    arrival_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    burst_time = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    memory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])