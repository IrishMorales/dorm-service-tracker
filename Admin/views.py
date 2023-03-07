from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import ServiceHourListing, User, Admins, Scholar, Assignment, Registration


class admin_view(TemplateView):
    template_name = "admin_view.html"


class scholars_listview(ListView):
    model = Scholar
    template_name = "scholar_list.html"
    queryset = Scholar.objects.all()


class signups_hoursview(ListView):
    model = ServiceHourListing
    template_name = "signups_hours.html"
    queryset = ServiceHourListing.objects.all()


def admin_scholar_white_card(request, user_id):
    registration = Registration.objects.select_related("serv_hours").get(
        scholar=user_id
    )
    scholar = Scholar.objects.get(scholar=user_id)

    return render(
        request,
        "scholars_white_card.html",
        {"registration": registration, "scholar": scholar},
    )


def admin_scholar_list_profile(request, user_id):
    registration = Registration.objects.select_related("serv_hours").get(
        scholar=user_id
    )
    scholar = Scholar.objects.get(scholar=user_id)
    return render(
        request,
        "admin_scholars_profile.html",
        {"registration": registration, "scholar": scholar},
    )
