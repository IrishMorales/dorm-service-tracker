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


def admin_scholar_white_card(request, user_id):
    scholar = Scholar.objects.get(pk=user_id)
    registration = Scholar.objects.get(user_id)
    servicehours = ServiceHourListing.objects.all()


# class signups_hours_createview(CreateView):

# class admin_scholar_list_profile_detailview(DetailView):
