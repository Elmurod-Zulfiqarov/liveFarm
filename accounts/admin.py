from django.contrib import admin
from .models import Accounts
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Accounts)
class AccountsAdmin(ImportExportActionModelAdmin):
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_display = ('username', 'email', 'phone', 'is_staff')
    list_filter = ('username', 'email')
