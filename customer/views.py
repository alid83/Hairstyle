from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from appointment.models import Appointment
from stylist.models import Services, TimeSlot
from account_module.models import Stylist, Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json




def list_appointments(request):
    if not request.user.is_authenticated:
        return redirect('login_page')

    upcoming_appointments = Appointment.objects.filter(
        customer=request.user,
        appointment_date__gte=now()
    )
    past_appointments = Appointment.objects.filter(
        customer=request.user,
        appointment_date__lt=now()
    )
    context = {
        "upcoming_appointments": upcoming_appointments,
        "past_appointments": past_appointments,
    }
    return render(request, "customer/appointments.html", context)



def reschedule_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect('login_page')

    appointment = get_object_or_404(Appointment, id=appointment_id, customer=request.user)

    if request.method == "POST":
        new_time_slot_id = request.POST.get("time_slot")
        new_time_slot = get_object_or_404(TimeSlot, id=new_time_slot_id)

        # Check policy constraints here (e.g., is rescheduling allowed?)
        if not appointment.status in ['pending', 'confirmed']:
            return redirect("customer:appointments")  # Redirect if rescheduling is not allowed

        appointment.time_slot = new_time_slot
        appointment.save()
        return redirect("customer:appointments")

    available_time_slots = TimeSlot.objects.filter(stylist=appointment.stylist)
    context = {"appointment": appointment, "time_slots": available_time_slots}
    return render(request, "customer/reschedule_appointment.html", context)



def cancel_appointment(request, appointment_id):
    if not request.user.is_authenticated:
        return redirect('login_page')

    appointment = get_object_or_404(Appointment, id=appointment_id, customer=request.user)

    # Check cancellation policy here (e.g., must cancel at least 24 hours in advance)
    if appointment.appointment_date <= now().date():
        return redirect("customer:appointments")  # Prevent cancellation if policy violated

    appointment.status = 'canceled'
    appointment.save()
    return redirect("customer:appointments")


@csrf_exempt
def appointment_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # داده‌ها را ذخیره کنید
        date = data['date']
        time = data['time']
        stylist = data['stylist']
        service = data['service']
        email = data['email']
        print(stylist)
        print(service)

        stylist = Stylist.objects.get(username=stylist)
        service = Services.objects.get(service_name=service, stylist=stylist)
        time_slot = TimeSlot.objects.get(start_time=time, stylist=stylist)
        customer = Customer.objects.get(id=request.user.id)

        Appointment.objects.create(
            customer=customer,
            stylist=stylist,
            service=service,
            time_slot=time_slot,
            appointment_date=date,
            status="pending",
        )

        # ذخیره در مدل (در صورت وجود)
        # appointment = Appointment.objects.create(**data)

        return JsonResponse({'message': 'Appointment created successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

