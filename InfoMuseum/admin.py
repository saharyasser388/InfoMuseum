from django.contrib import admin
from . import models
from . import *
from InfoMuseum.models import Openning_Hour
# Register your models here.
'''
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'date', 'start_time', 'end_time']
    ordering = ['date']


@admin.register(models.Openning_Hour)
class Openning_HourAdmin(admin.ModelAdmin):
    list_per_page = 7
    list_display = ['day', 'open_time', 'close_time']
    ordering = ['day']   

@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name']

@admin.register(models.Museum_Info)
class Museum_InfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'address', 'contact_mail','contact_phone','halls_number','about']
    
class Museum_InfoAdminInline(admin.StackedInline):
    model = models.Museum_Info
'''
admin.site.register(models.Event)
admin.site.register(models.Media)
admin.site.register(models.Museum_Info)
admin.site.register(models.Openning_Hour)