from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Admins, Registration, Scholar, ServiceHourListing,User


def get_admin(request):

    admin = Admins.objects.all()
    registration = Registration.objects.all()
    scholar = Scholar.objects.all()
    serviceHourListing = ServiceHourListing.objects.all()
    user = User.objects.all()
    context = {
        'admin': admin,
        'registration': registration,
        'scholar': scholar,
        'serviceHourListing': serviceHourListing,
        'user': user
    }
    return render(request, 'Admin/admin.html', context)
