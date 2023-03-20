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
