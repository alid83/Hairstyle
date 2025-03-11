from django.contrib import admin
from .models import Customer,User,Stylist
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')  # ستون‌هایی که می‌خواهید نمایش داده شوند
    list_filter = ('is_active',)  # فیلترهایی برای مرتب‌سازی و جستجو
    search_fields = ('email', 'first_name', 'last_name')  # جستجو بر اساس فیلدهای مختلف

# ثبت مدل Stylist در پنل مدیریت
@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active')  # ستون‌هایی که می‌خواهید نمایش داده شوند
    list_filter = ('is_active',)  # فیلترهایی برای مرتب‌سازی و جستجو
    search_fields = ('email', 'first_name', 'last_name')  # جستجو بر اساس فیلدهای مختلف

# ثبت مدل User در پنل مدیریت
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_hairstyle')  # ستون‌هایی که می‌خواهید نمایش داده شوند
    list_filter = ('is_active', 'is_hairstyle')  # فیلترهایی برای مرتب‌سازی و جستجو
    search_fields = ('email', 'first_name', 'last_name')  # جستجو بر اساس فیلدهای مختلف