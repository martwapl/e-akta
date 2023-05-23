from django.contrib import admin
from .models import Profile, Case, File, SendEmail, Event
# Register your models here.
admin.site.register(Profile)
admin.site.register(Case)
admin.site.register(File)
admin.site.register(SendEmail)
admin.site.register(Event)
