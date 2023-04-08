from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.contrib.auth.decorators import login_required

# TODO: Add if-else block here so that it redirects to admin view if user is admin, scholar view if user is scholar
@login_required
def login_redirect(request):
    # TODO: THIS IS A TEMPORARY WORKAROUND TO GET URLS WITH USER ID TO WORK - IT ALWAYS REDIRECTS TO USER 200000
    return HttpResponseRedirect(f"user_scholar/200000")
    # TODO: BELOW IS THE PROPER WAY TO REDIRECT BASED ON THE USER'S ID
    # For now, this works for login but not for any of the profile, white card, admin pages because
    # the Django project still uses Django's AuthUser model for login, not our project's custom User model
    # Once the login is configured to use the custom User model, uncomment the line below
    # return HttpResponseRedirect(f"user_scholar/{request.user.id}")


# General URLs
urlpatterns = [
    path("login_redirect", login_redirect, name="login_redirect"),
    path("admin/", admin.site.urls),
    path("", auth_views.LoginView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
    path("user_scholar/", include("Scholar.urls", namespace="Scholar")),
    path("user_admin/", include("Admin.urls", namespace="Admin")),
]
