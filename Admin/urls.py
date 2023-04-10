from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth.decorators import login_required


from Admin.views import (
    admin_scholar_white_card,
    admin_scholar_list_profile,
    admin_add_slots,
    admin_view,
    scholars_listview,
    signups_hoursview,
)

urlpatterns = [
    path("", login_required(admin_view.as_view()), name="admin_view"),
    path("scholars_list/", (scholars_listview.as_view()), name="scholars-listview"),
    path(
        "signup_hours/",
        (signups_hoursview.as_view()),
        name="signup-hours-listview",
    ),
    path(
        "scholars_list/white_card/<int:user_id>",
        admin_scholar_white_card,
        name="admin-scholar-white-card",
    ),
    path(
        "scholars_list/profile/<int:user_id>",
        admin_scholar_list_profile,
        name="admin-scholar-profile",
    ),
    path("signup_hours/add_slots/", admin_add_slots, name="admin-add-slots"),
]

app_name = "Admin"
