from django.contrib import admin
from .models import ServiceRequest
from .models import *

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_type', 'urgency', 'created_at')
    list_filter = ('service_type', 'urgency', 'created_at')
    search_fields = ('name', 'email', 'message')

