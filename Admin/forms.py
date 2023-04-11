from django import forms
from django.forms.widgets import SelectDateWidget
from .models import ServiceHourListing

LOCATIONS = (
    ("Eliazo", "Eliazo"),
    ("Cervini", "Cervini"),
    ("IRH", "IRH"),
    ("UD", "UD"),
)

START_TIMES = (
    ("08:00", "08:00"),
    ("09:30", "09:30"),
    ("11:00", "11:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:30", "15:30"),
)

END_TIMES = (
    ("09:30", "09:30"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("14:00", "14:00"),
    ("15:30", "15:30"),
    ("17:00", "17:00"),
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


class EditSlot(forms.Form):
    # TODO: Change initial value of fields to the current value of the slot (ex. current date before editing, etc.)
    serv_hours_task = forms.CharField()
    serv_hours_loc = forms.ChoiceField(choices=LOCATIONS)
    serv_hours_date = forms.DateField(widget=SelectDateWidget())
    # TODO: Add way to validate that serv_hours_end_time should be later than serv_hours_start_time
    serv_hours_start_time = forms.ChoiceField(choices=START_TIMES)
    serv_hours_end_time = forms.ChoiceField(choices=END_TIMES)

    class Meta:
        model = ServiceHourListing

    def __init__(self, *args, **kwargs):
        super(EditSlot, self).__init__(*args, **kwargs)
