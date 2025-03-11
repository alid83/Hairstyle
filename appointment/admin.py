from django.contrib import admin
from .models import Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'stylist', 'service', 'appointment_date', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('customer__email', 'stylist__email', 'service__service_name')