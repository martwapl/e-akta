from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class SendEmail(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=128)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.sender


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150, blank=False)
    phone = models.CharField(max_length=16, blank=True)
    address = models.TextField(null=True, blank=True)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


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
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(choices=CASE_STATUS)
    category = models.CharField(choices=CATEGORY)
    mail = models.EmailField(max_length=150, blank=True)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=32)
    file = models.FileField(max_length=64,
                            validators=[FileExtensionValidator(['pdf'])])
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return self.case

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
