# Generated by Django 3.2.8 on 2021-10-19 17:29

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('covid_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='result',
            field=models.CharField(default='Unknown', max_length=8),
        ),
        migrations.AddField(
            model_name='users',
            name='risk',
            field=models.SmallIntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='users',
            name='userid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]