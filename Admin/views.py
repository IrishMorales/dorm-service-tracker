from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Admins, Registration, Scholar, ServiceHourListing,User


def get_admin(request):

    user = User.objects.all().order_by('user_id')
    admin = Admins.objects.all()
    registration = Registration.objects.all()
    scholars = Scholar.objects.all()
    service_hours = ServiceHourListing.objects.all()

    context = {
        'users': user,
        'admins': admin,
        'registration': registration,
        'scholars': scholars,
        'service_hours': service_hours

    }

    return render(request, 'Admin/admin.html', context)
