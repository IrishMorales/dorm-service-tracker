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


def scholar_enlist_slots(request, reg_id, user_id):
    scholar_details = Scholar.objects.get(pk=user_id)
    user_details = User.objects.get(pk=user_id)
    registration = Registration.objects.select_related("serv_hours").filter(
        scholar_id__isnull=True
    )

    # build the URL for the 'scholar_enlist_slots' view with the user ID and registration ID
    url = reverse("scholar_enlist_slots", kwargs={"reg_id": reg_id, "user_id": user_id})

    if request.method == "POST":
        form = EnlistSlot(request.POST, request.FILES)
        if form.is_valid():
            reg_id = form.cleaned_data.get("reg_id")
            user_id = form.cleaned_data.get("user_id")

            reg = Registration.objects.get(reg_id=reg_id)
            reg.scholar = user_id
            reg.save()

            return redirect("Scholar:scholar_view_profile")
    else:
        form = EnlistSlot()
    return render(
        request,
        "scholar_hours_signup.html",
        {
            "form": form,
            "registration": registration,
            "user_details": user_details,
            "scholar_details": scholar_details,
        },
    )
