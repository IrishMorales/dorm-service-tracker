from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path("<int:user_id>/", login_required(scholar_view.as_view()), name="scholar_view"),
    path('<int:user_id>/profile/', view_profile, name='scholar_view_profile'),
    path('<int:user_id>/white_card/', scholar_white_card, name='scholar_white_card'),
]

app_name = "Scholar"
