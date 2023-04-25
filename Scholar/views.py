from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import *
from .forms import *


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
    registration = Registration.objects.select_related("serv_hours").filter(
        scholar=user_id
    )
    registration_details = Registration.objects.filter(scholar=user_id)
    service_hours = ServiceHourListing.objects.filter(registration__scholar=user_id)
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


def scholar_hours_signup(request, user_id):
    scholar_details = Scholar.objects.get(pk=user_id)
    user_details = User.objects.get(pk=user_id)
    registration = Registration.objects.select_related("serv_hours").filter(
        scholar_id__isnull=True
    )

    return render(
        request,
        "scholar_hours_signup.html",
        {
            "registration": registration,
            "user_details": user_details,
            "scholar_details": scholar_details,
        },
    )


def scholar_enlist_slot(request, user_id, reg_id):
    scholar_details = Scholar.objects.get(pk=user_id)
    user_details = User.objects.get(pk=user_id)
    registration = Registration.objects.select_related("serv_hours").filter(
        scholar_id__isnull=True
    )
    if request.method == "POST":
        url = reverse("Scholar:scholar_view_profile", args=[user_id, reg_id])

        enlisted_slot = Registration.objects.get(reg_id=reg_id)
        enlisted_slot.scholar_id = user_id
        enlisted_slot.save()

        return redirect(url)
    else:
        # Handle GET request
        return render(
            request,
            "scholar_hours_signup.html",
            {
                "registration": registration,
                "user_details": user_details,
                "scholar_details": scholar_details,
            },
        )
