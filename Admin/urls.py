from django.urls import path

from Admin.views import (
    admin_view,
    scholars_listview,
    signups_hours_listview,
    admin_scholar_white_card,
    admin_scholar_list_profile,
)

urlpatterns = [
    path("scholars_list/", (scholars_listview.as_view()), name="scholars-listview"),
    path(
        "signup_hours/",
        (signups_hours_listview.as_view()),
        name="signup-hours-listview",
    ),
    path(
        "scholars_list/white_card/<int:user_id>",
        admin_scholar_white_card,
        name="admin_scholar_white_chard",
    ),
    path(
        "scholars_list/profile/<int:user_id>",
        admin_scholar_list_profile,
        name="admin_scholar_profile",
    ),
]
