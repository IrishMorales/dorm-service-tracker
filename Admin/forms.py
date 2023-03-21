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
