from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import ServiceHourListing, User, Admins, Scholar, Assignment, Registration
from .forms import AddListing
from datetime import datetime, timedelta



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

def view_add_listing(request):
    if request.method == 'POST':
        form = AddListing(request.POST, request.FILES)
        if form.is_valid():
            slot_count = form.cleaned_data.get('serv_hours_slot_count')
            location = form.cleaned_data.get('serv_hours_loc')
            task = form.cleaned_data.get('serv_hours_task')
            times = ["08:00", "09:30", "11:00", "01:00", "14:00", "15:30"]
            start_date = datetime.strptime(form.cleaned_data.get('serv_hours_date_start'), '%Y-%m-%d').date()
            end_date = datetime.strptime(form.cleaned_data.get('serv_hours_date_end'), '%Y-%m-%d').date() + timedelta(days=1)
            for single_date in daterange(start_date, end_date):
                date = single_date.strftime("%Y-%m-%d")
                for time in times:
                    listing = ServiceHourListing(serv_hours_date = date, serv_hours_time = time, serv_hours_loc = location, serv_hours_slot_count = slot_count, serv_hours_task = task)
                    listing.save()
            return redirect() #TODO: idk where this redirects
    else:
        form = AddListing()
    return render(request, 'addTicket.html', {'form': form, }) #TODO: idk what this renders

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

