from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ('name', 'summary', 'image')
    list_display = ('name', 'summary', 'image')
    list_display_links = ('name', 'summary', 'image')
    list_filter = ('name', 'summary', 'image')
    

