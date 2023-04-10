from django import forms
from django.forms.widgets import SelectDateWidget
from .models import ServiceHourListing

LOCATIONS = (
    ("Eliazo", "Eliazo"),
    ("Cervini", "Cervini"),
    ("IRH", "IRH"),
    ("UD", "UD"),
)


class AddSlot(forms.Form):
    serv_hours_task = forms.CharField()
    serv_hours_loc = forms.ChoiceField(choices=LOCATIONS)
    serv_hours_slot_count = forms.IntegerField()
    serv_hours_date_start = forms.DateField(widget=SelectDateWidget())
    serv_hours_date_end = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = ServiceHourListing

    def __init__(self, *args, **kwargs):
        super(AddSlot, self).__init__(*args, **kwargs)
