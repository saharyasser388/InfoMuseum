from django.contrib import admin
from .models import ArtObject
from . import models
# Register your models here.


@admin.register(models.Hall)
class HallAdmin(admin.ModelAdmin):
    list_per_page = 50


@admin.register(models.Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_per_page = 50

@admin.register(models.ArtStory)
class ArtStoryAdmin(admin.ModelAdmin):
    list_per_page = 50

@admin.register(models.BorrowedCollection)
class BorrowedCollectionAdmin(admin.ModelAdmin):
    list_per_page = 50 
@admin.register(models.PermenantCollection)
class PermenantCollectionAdmin(admin.ModelAdmin):
    list_per_page = 50

@admin.register(models.Other)
class OtherAdmin(admin.ModelAdmin):
    list_per_page = 50

@admin.register(models.Chariot)
class ChariotAdmin (admin.ModelAdmin):
    list_per_page = 50

@admin.register(models.Painting)
class PaintingAdmin(admin.ModelAdmin):
    list_per_page = 50

@admin.register(models.Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_per_page = 50


    
class DescriptionInline (admin.TabularInline):
    model = models.Description
 
class ArtStoryAdminInline(admin.StackedInline):
    model = models.ArtStory

class BorrowedCollectionAdminInline(admin.TabularInline):
    model = models.BorrowedCollection

class PermenantCollectionAdminInline(admin.TabularInline):
    model = models.PermenantCollection

class ChariotInline(admin.TabularInline):
    model = models.Chariot

class OtherInline(admin.TabularInline):
    model = models.Other

class HoldingInline(admin.TabularInline):
    model = models.Holding

class PaintingInline(admin.TabularInline):
    model = models.Painting


@admin.register(models.ArtObject)
class ArtObjectAdmin(admin.ModelAdmin):
    inlines = [DescriptionInline ,ArtStoryAdminInline,BorrowedCollectionAdminInline, PermenantCollectionAdminInline, PaintingInline, ChariotInline,OtherInline,HoldingInline ]
    #fields = ['name']
    list_per_page = 5 
    list_filter = ['hall']
    search_fields = ['name']
    list_display = ['name','hall','Description', 'ArtStory']
    list_editable = ['hall']



 


