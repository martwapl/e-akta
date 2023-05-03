from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="/uploads/%Y/%m/%d")

# Create your models here.
class Case(models.Model):
    CASE_STATUS = {
        ('Czeka na dekretację', 'Czeka na dekretację'),
        ('Zadekretowana', 'Zadekretowana'),
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
    number = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(choices=CASE_STATUS)
    category = models.CharField(choices=CATEGORY)

class File(models.Model):
    name = models.CharField(max_length=32)
    file = models.FileField(storage=fs)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

