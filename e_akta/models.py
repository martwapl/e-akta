from django.db import models
from django.contrib.auth.models import User, Group, Permission, PermissionsMixin
from django.core.validators import FileExtensionValidator
import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Case(models.Model):
    CASE_STATUS = {
        ('W toku', 'W toku'),
        ('Zakończona', 'Zakończona'),
        ('Zarchiwizowana', 'Zarchiwizowana'),
    }
    CATEGORY = {
        ('Prawo karne', 'Prawo karne'),
        ('Prawo cywilne', 'Prawo cywilne'),
        ('Prawo administracyjne', 'Prawo administracyjne'),
        ('Prawo pracy', 'Prawo pracy'),
        ('Prawo rodzinne', 'Prawo rodzinne'),
    }
    name = models.CharField(max_length=128)
    number = models.PositiveIntegerField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(choices=CASE_STATUS)
    category = models.CharField(choices=CATEGORY, default='Prawo karne')

class File(models.Model):
    name = models.CharField(max_length=32)
    file = models.FileField(max_length=25, validators=[FileExtensionValidator(['pdf'])])
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    place = models.CharField(max_length=64, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

