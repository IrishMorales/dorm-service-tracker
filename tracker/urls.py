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
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from homepage.views import home_view
from scholar_profile.views import profile_view
from white_card.views import white_card_view
from Admin.views import admin_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # includes pages for login, logout, password changess
    path("", login_required(home_view.as_view()), name="home"),
    path("profile/", login_required(profile_view.as_view()), name="profile"),
    path("white_card/", login_required(white_card_view.as_view()), name="white_card"),
    path("user_admin/", include("Admin.urls"), name="admin_view"),
]
