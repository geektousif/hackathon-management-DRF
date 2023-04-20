from django.contrib import admin

from .models import Submission, Image, File,Link
# Register your models here.
admin.site.register(Submission)
admin.site.register(Image)
admin.site.register(File)
admin.site.register(Link)