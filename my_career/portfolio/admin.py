from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('status', 'created_at')
    fields = ('first_name', 'last_name', 'email', 'phone', 'resume', 'status', 'created_at')
    readonly_fields = ('created_at',)

