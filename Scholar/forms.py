from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Registration


class EnlistSlot(forms.Form):
    reg_id = forms.IntegerField()
    scholar_id = forms.IntegerField()
    serv_hours_id = forms.IntegerField()

    class Meta:
        managed = False
        db_table = "registration"

    def __init__(self, *args, **kwargs):
        super(EnlistSlot, self).__init__(*args, **kwargs)
