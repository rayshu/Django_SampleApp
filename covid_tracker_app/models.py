from django.db import models
from django import forms
from django.core.validators import RegexValidator
import uuid

class Users(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])
    risk = models.SmallIntegerField(default=-1)
    result = models.CharField(max_length=8, default='Unknown')