from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import *


class scholar_view(TemplateView):
    template_name = "scholar_view.html"

    model = User
    slug_field = "id"


def view_profile(request, user_id):
    user_details = User.objects.get(pk=user_id)
    scholar_details = Scholar.objects.get(pk=user_id)
    servHoursListing_details = ServiceHourListing.objects.all()
    return render(
        request,
        "scholar_profile.html",
        {
            "user_details": user_details,
            "scholar_details": scholar_details,
            "servHoursListing_details": servHoursListing_details,
        },
    )


def scholar_white_card(request, user_id):
    scholar_details = Scholar.objects.get(pk=user_id)
    user_details = User.objects.get(pk=user_id)
    registration_details = Registration.objects.get(scholar=user_id)
    service_hours = ServiceHourListing.objects.filter(
        serv_hours_id=registration_details.reg_id
    )
    return render(
        request,
        "scholar_white_card.html",
        {
            "registration": registration,
            "user_details": user_details,
            "scholar_details": scholar_details,
            "servHoursListing_details": service_hours,
        },
    )
