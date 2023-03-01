from django.urls import path
from .views import *

# Create your views here.

urlpatterns = [
    path('', get_admin, name='admin'),
]

app_name = 'Admin'