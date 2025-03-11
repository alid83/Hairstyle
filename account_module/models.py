from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    is_hairstyle = models.BooleanField(default=False)

    # تعریف نام‌های مرتبط سفارشی برای حل تداخل
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # دسترسی معکوس سفارشی برای گروه‌ها
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # دسترسی معکوس سفارشی برای دسترسی‌ها
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()


class Stylist(User):
    user_image = models.ImageField()
    status = models.BooleanField()
    rating = models.FloatField()
    address = models.CharField(max_length=500)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'آرایشگر'
        verbose_name_plural = 'آرایشگران'


    def __str__(self):
        return self.get_full_name()


class Customer(User):

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    def __str__(self):
        return self.get_full_name()