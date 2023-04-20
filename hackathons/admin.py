from django.contrib import admin

from .models import Hackathon, Enrollment
# Register your models here.
admin.site.register(Hackathon)
admin.site.register(Enrollment)