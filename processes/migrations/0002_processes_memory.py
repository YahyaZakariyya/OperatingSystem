# Generated by Django 4.2 on 2023-05-19 20:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processes',
            name='memory',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]