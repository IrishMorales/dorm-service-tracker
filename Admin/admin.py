from django.contrib import admin

# Register your models here.
from .models import Admins, Assignment, Registration, Scholar, ServiceHourListing, User

admin.site.register(Admins)
admin.site.register(Assignment)
admin.site.register(Registration)
admin.site.register(Scholar)
admin.site.register(ServiceHourListing)
admin.site.register(User)