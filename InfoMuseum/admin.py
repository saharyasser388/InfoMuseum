from django.contrib import admin
from . import models
from . import *
from InfoMuseum.models import Openning_Hour
# Register your models here.


@admin.register(models.Openning_Hour)
class Openning_HoursAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['day', 'open_time', 'close_time']

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['name','date','start_time','end_time', 'event_about']

@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_per_page = 50 
    list_display = ['media', 'name']
'''

admin.site.register(models.Openning_Hour)
admin.site.register(models.Event)
admin.site.register(models.Media)
'''
    
class MediaInline (admin.TabularInline):
    model = models.Media
 
class EventAdminInline(admin.StackedInline):
    model = models.Event

class Museum_InfoAdminInline(admin.TabularInline):
    model = models.Museum_Info

class Openning_HoursAdminInline(admin.TabularInline):
    model = models.Openning_Hour



@admin.register(models.Museum_Info)
class Museum_InfoAdmin(admin.ModelAdmin):
    inlines = [Openning_HoursAdminInline ,EventAdminInline, MediaInline]
    #fields = ['name']
    list_per_page = 5 

    list_display = [ 'openning_Hours','Events']

    
    '''
    list_filter = ['hall']
    search_fields = ['name']
    
    list_editable = ['hall']
    '''
    
