from django.contrib import admin
from .models import Pet, Milk, Fodder, Farm
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Farm)
class FarmAdmin(ImportExportActionModelAdmin):
    search_fields = ('name', 'owner')
    list_display = ('name', 'owner', 'address')
    list_filter = ('name', 'owner', 'address')


@admin.register(Pet)
class PetAdmin(ImportExportActionModelAdmin):
    search_fields = ('name', 'category')
    list_display = ('name', 'category', 'age', 'sold')
    list_filter = ('name', 'age', 'category', 'sold')


@admin.register(Milk)
class MilkAdmin(ImportExportActionModelAdmin):
    search_fields = ('cow_id', 'liters', 'date')
    autocomplete_fields = ('cow_id',)
    list_display = ('cow_id', 'liters', 'date')
    list_filter = ('cow_id', 'liters', 'date')


@admin.register(Fodder)
class FodderAdmin(ImportExportActionModelAdmin):
    search_fields = ('title', 'date')
    list_display = ('title', 'cost', 'size', 'date')
    list_filter = ('title', 'cost', 'size', 'date')


