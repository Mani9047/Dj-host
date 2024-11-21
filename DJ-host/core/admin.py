from django.contrib import admin
from .models import FileUpload



@admin.register(FileUpload)
class HostingPlanAdmin(admin.ModelAdmin):
    list_display =['user','file']