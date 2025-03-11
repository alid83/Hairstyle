import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from account_module.models import Stylist, User
from django.shortcuts import render
from django.core.paginator import Paginator
from stylist.models import Services, TimeSlot
from appointment.models import Appointment


def get_stylists(request):
    if not request.user.is_authenticated:
        return redirect('login_page')

    user = request.user
    services = Services.objects.all()
    # if request.method == 'POST':
    #     province = request.POST.get('province')
    #     city = request.POST.get('city')
    #     if province and city:
    #         stylists = Stylist.objects.filter(province = province, city = city).order_by('rating')
    #         paginator = Paginator(stylists, 10)
    #         page_number = request.GET.get('page')
    #         page_obj = paginator.get_page(page_number)
    #         return render(request, 'stylist/customerIndex.html', {'page_obj': page_obj})
    #     elif province:
    #         stylists = Stylist.objects.filter(province = province).order_by('rating')
    #         paginator = Paginator(stylists, 10)
    #         page_number = request.GET.get('page')
    #         page_obj = paginator.get_page(page_number)
    #         return render(request, 'stylist/customerIndex.html', {'page_obj': page_obj})
    stylists = Stylist.objects.all().order_by('rating')
    return render(request, 'stylist/customerIndex.html', {'stylists': stylists, 'user' : user, 'services': services})

def get_stylist(request, stylist_id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    stylist = get_object_or_404(Stylist, id=stylist_id)
    services = stylist.services.all()
    time_slots = stylist.time_slots.all()
    stylists = Stylist.objects.all()

    context = {
        'stylist': stylist,
        'services': services,
        'time_slots': time_slots,
        'stylists': stylists,
    }
    return render(request, 'stylist/detail.html', context)

def stylist_view(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    stylist = User.objects.filter(id=request.user.id).first()
    appointment = Appointment.objects.filter(stylist=stylist).first()
    services = Services.objects.filter(stylist=stylist).all()
    time_slots = TimeSlot.objects.filter(stylist=stylist).all()
    context = {
        'stylist': stylist,
        'appointment': appointment,
        'services': services,
        'time_slots': time_slots,
    }
    return render(request, 'stylist/stylistIndex.html', context)

@csrf_exempt
def new_time(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        start_time = data.get('start')
        end_time = data.get('end')
        date = data.get('date')
        id = request.user.id
        stylist = Stylist.objects.filter(id=id).first()
        print(start_time, end_time, stylist)
        # ایجاد سرویس جدید
        time = TimeSlot.objects.create(
            stylist=stylist,
            start_time=start_time,
            end_time=end_time,
            date=date,
            is_recurring=False,
            day_of_week=None,
        )
        time.save()
        print(time)
        # ذخیره در مدل (در صورت وجود)
        # appointment = Appointment.objects.create(**data)

        return JsonResponse({'message': 'Appointment created successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def new_service(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        service_name = data.get('service')
        service_price = data.get('price')
        service_description = data.get('description')
        service_duration = data.get('duration')
        id = request.user.id
        stylist = Stylist.objects.filter(id=id).first()

        # ایجاد سرویس جدید
        service = Services.objects.create(
            stylist=stylist,
            service_name=service_name,
            price=service_price,
            service_description=service_description,
            duration=service_duration,
        )
        service.save()
        print(service)
        # ذخیره در مدل (در صورت وجود)
        # appointment = Appointment.objects.create(**data)

        return JsonResponse({'message': 'Appointment created successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def my_data(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    stylist = User.objects.filter(id=request.user.id).first()
    appointment = Appointment.objects.filter(stylist=stylist).all()
    services = Services.objects.filter(stylist=stylist).all()
    time_slots = TimeSlot.objects.filter(stylist=stylist).all()
    context = {
        'stylist': stylist,
        'appointments': appointment,
        'services': services,
        'time_slots': time_slots,
    }
    return render(request, 'stylist/my_data.html', context)