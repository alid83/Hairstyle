from django.db import models

from account_module.models import Customer, Stylist
from stylist.models import Services, TimeSlot


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, related_name="appointments", on_delete=models.CASCADE)
    stylist = models.ForeignKey(Stylist, related_name="appointments", on_delete=models.CASCADE)
    service = models.ForeignKey(Services, related_name="appointments", on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, related_name="appointments", on_delete=models.CASCADE)
    appointment_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled'),
        ],
        default='pending'
    )

    def is_upcoming(self):
        from django.utils.timezone import now
        return self.appointment_date >= now().date()
