"""tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from Admin.views import admin_view, scholars_listview
from Scholar.views import scholar_view, profile_view, white_card_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", auth_views.LoginView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
    path("user_scholar/", login_required(scholar_view.as_view()), name="scholar_view"),
    path(
        "user_scholar/profile/", login_required(profile_view.as_view()), name="profile"
    ),
    path(
        "user_scholar/white_card/",
        login_required(white_card_view.as_view()),
        name="white_card",
    ),
    path("user_admin/", login_required(admin_view.as_view()), name="admin_view"),
    path(
        "user_admin/scholars_list/",
        login_required(scholars_listview.as_view()),
        name="scholars-listview",
    ),
    # is this for the login_required thing
    # the what what is the this
]
