from django.contrib import admin
from .models import TimeSlot, Services, Tokenism, Images

# Register your models here.
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('stylist', 'date', 'start_time', 'end_time', 'is_recurring')
    list_filter = ('stylist', 'date', 'is_recurring')
    search_fields = ('stylist__username', 'date')

# ثبت مدل Services در بخش admin
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_description', 'duration', 'price', 'stylist')
    list_filter = ('stylist',)
    search_fields = ('service_name', 'stylist__username')

# ثبت مدل Tokenism در بخش admin
class TokenismAdmin(admin.ModelAdmin):
    list_display = ('service', 'description')
    search_fields = ('service__service_name', 'description')

# ثبت مدل Images در بخش admin
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'tokenism')
    list_filter = ('tokenism',)

# ثبت هر مدل در admin
admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Tokenism, TokenismAdmin)
admin.site.register(Images, ImagesAdmin)