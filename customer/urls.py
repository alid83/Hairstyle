from django.urls import path
from . import views

app_name = "customer"

urlpatterns = [
    path("appointments/", views.list_appointments, name="appointments"),
    path("appointments/<int:appointment_id>/reschedule/", views.reschedule_appointment, name="reschedule_appointment"),
    path("appointments/<int:appointment_id>/cancel/", views.cancel_appointment, name="cancel_appointment"),
    path('appointment/', views.appointment_view, name='appointment'),
]
