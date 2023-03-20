<<<<<<< HEAD
from django import forms
from .models import ServiceHourListing

class AddSlot(forms.ModelForm):
    class Meta:
        model = ServiceHourListing
        fields = ['serv_hours_date',
                  'serv_hours_start_time',
                  'serv_hours_end_time',
                  'serv_hours_loc',
                  'serv_hours_slot_count',
]

        labels = {      
            'serv_hours_date': 'Date',
            'serv_hours_start_time': 'Start Time',
            'serv_hours_end_time': 'End Time',
            'serv_hours_loc': 'Building',
            'serv_hours_slot_count': 'Slot Count',
        }

    def __init__(self, *args, **kwargs):
        super(AddSlot, self).__init__(*args, **kwargs)
=======
from django import forms
from .models import ServiceHourListing

class AddListing(forms.ModelForm):
    class Meta:
        model = ServiceHourListing
        fields = 'serv_hours_date_start', 'serv_hours_date_end', 'serv_hours_time', 'serv_hours_loc', 'serv_hours_slot_count', 'serv_hours_task'

        labels = {      
            
        }

    def __init__(self, *args, **kwargs):
        super(AddCustomer, self).__init__(*args, **kwargs)
>>>>>>> 3002359 (added forms.py to admin, added automation script to views.py in admin)
