
from django.contrib import admin
from .models import User, EmployerProfile, Job

admin.site.register(User)
admin.site.register(EmployerProfile)
admin.site.register(Job)