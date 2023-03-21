from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import ServiceHourListing, User, Admins, Scholar, Assignment, Registration
from .forms import AddSlot

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

def admin_add_slots(request):
    registration = Registration.objects.all()
    if request.method == 'POST':
        form = AddSlot(request.POST, request.FILES)
        if form.is_valid():
            new_slot = form.save()
            return redirect('signup_hours/add_slots')
    else:
        form = AddSlot()
    return render(request, "admin_add_slots.html", {'form':form, 'registration':registration})
