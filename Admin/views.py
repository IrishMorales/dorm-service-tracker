from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import ServiceHourListing, User, Admins, Scholar, Assignment, Registration
from .forms import AddSlot
from datetime import datetime, timedelta

class admin_view(TemplateView):
    template_name = "admin_view.html"


class scholars_listview(ListView):
    model = Scholar
    template_name = "admin_scholar_list.html"
    queryset = Scholar.objects.all()


class signups_hoursview(ListView):
    model = ServiceHourListing
    template_name = "admin_signups_hours.html"
    queryset = ServiceHourListing.objects.all()


def admin_scholar_white_card(request, user_id):
    registration = Registration.objects.select_related("serv_hours").filter(
        scholar=user_id)
    scholar_details = Scholar.objects.get(scholar=user_id)

    return render(
        request,
        "admin_scholar_whitecard.html",
        {"registration": registration, "scholar_details": scholar_details},
    )


def admin_scholar_list_profile(request, user_id):
    registration = Registration.objects.select_related("serv_hours").filter(
        scholar=user_id
    )
    scholar_details = Scholar.objects.get(scholar=user_id)
    return render(
        request,
        "admin_scholar_profile.html",
        {"registration": registration, "scholar_details": scholar_details},
    )

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def admin_add_slots(request):
    registration = Registration.objects.all()
    if request.method == 'POST':
        form = AddSlot(request.POST, request.FILES)
        if form.is_valid():
            slot_count = form.cleaned_data.get('serv_hours_slot_count')
            location = form.cleaned_data.get('serv_hours_loc')
            task = form.cleaned_data.get('serv_hours_task')
            start_times = ["08:00", "09:30", "11:00", "013:00", "14:00", "15:30"]
            end_times = ["09:30", "11:00", "12:00", "14:00", "15:30", "17:00"]
            start_date = datetime.strptime(form.cleaned_data.get('serv_hours_date_start'), '%Y-%m-%d').date()
            end_date = datetime.strptime(form.cleaned_data.get('serv_hours_date_end'), '%Y-%m-%d').date() + timedelta(days=1)
            for single_date in daterange(start_date, end_date):
                date = single_date.strftime("%Y-%m-%d")
                for start_time, end_time in zip(start_times, end_times):
                    listing = ServiceHourListing(serv_hours_date = date, serv_hours_start_time = start_time, serv_hours_end_time = end_time, serv_hours_loc = location, serv_hours_slot_count = slot_count, serv_hours_task = task)
                    listing.save()
            return redirect('signup_hours/add_slots')
    else:
        form = AddSlot()
    return render(request, "admin_add_slots.html", {'form':form, 'registration':registration})