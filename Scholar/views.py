from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import *


def scholar_view(TemplateView):
    template_name = "scholar_view.html"


def view_profile(request, user_id):
    personal_information = User.objects.get(pk=user_id)
    hours_rendered = Scholar.hours_rendered.get(pk=user_id)
    hours_needed = hours_rendered + Scholar.hours_needed.get(pk=user_id)
    service_hours = ServiceHourListing.objects.all()
    return render(
        request,
        "personal_information.html",
        {
            "personal_information": personal_information,
            "hours_rendered": hours_rendered,
            "hours_needed": hours_needed,
            "service_hours": service_hours,
        },
    )


def scholar_white_card(request, user_id):
    scholar = Scholar.objects.get(pk=user_id)
    registration = Scholar.objects.get(user_id)
    servicehours = ServiceHourListing.objects.all()
