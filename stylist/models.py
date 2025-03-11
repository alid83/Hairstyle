from django.db import models
from django.db import models
from account_module.models import Stylist
from .functions import to_jalali


class TimeSlot(models.Model):
    stylist = models.ForeignKey(Stylist, related_name="time_slots", on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)  # تاریخ خاص برای زمان‌بندی
    start_time = models.TimeField()  # شروع بازه زمانی
    end_time = models.TimeField()  # پایان بازه زمانی
    is_recurring = models.BooleanField(default=False)  # آیا زمان‌بندی تکرار شونده است؟
    day_of_week = models.IntegerField(
        null=True, blank=True, choices=[
            (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
            (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')
        ]
    )

    # روز هفته برای زمان‌بندی‌های تکرار شونده
    def get_persian_day_of_week(self):
        days = {
            0: 'دوشنبه',
            1: 'سه‌شنبه',
            2: 'چهارشنبه',
            3: 'پنج‌شنبه',
            4: 'جمعه',
            5: 'شنبه',
            6: 'یک‌شنبه',
        }
        return days.get(self.day_of_week, 'نامشخص')

    def get_jalali_date(self):
        if self.date:
            return to_jalali(self.date)
        return None

    class Meta:
        unique_together = ('stylist', 'date', 'start_time', 'end_time')
        ordering = ['date', 'start_time']

    def __str__(self):
        if self.is_recurring:
            return f"{self.stylist.username} - {self.get_day_of_week_display()} ({self.start_time}-{self.end_time})"
        else:
            return f"{self.stylist.username} - {self.date} ({self.start_time}-{self.end_time})"


class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=255)
    duration = models.FloatField()
    price = models.FloatField()
    stylist = models.ForeignKey(Stylist, related_name="services", on_delete=models.CASCADE)


class Tokenism(models.Model):
    service = models.ForeignKey(Services, related_name='tokenism', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)


class Images(models.Model):
    image = models.ImageField()
    tokenism = models.ForeignKey(Tokenism, related_name='images', on_delete=models.CASCADE)
