from django.db import models

# Create your models here.
class Admins(models.Model):
    admin = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class Assignment(models.Model):
    assignment_id = models.IntegerField(primary_key=True)
    admin = models.ForeignKey(Admins, models.DO_NOTHING, blank=True, null=True)
    serv_hours = models.ForeignKey('ServiceHourListing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'


class Registration(models.Model):
    reg_id = models.IntegerField(primary_key=True)
    scholar = models.ForeignKey('Scholar', models.DO_NOTHING, blank=True, null=True)
    serv_hours = models.ForeignKey('ServiceHourListing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration'


class Scholar(models.Model):
    scholar = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    hours_needed = models.IntegerField(blank=True, null=True)
    hours_rendered = models.IntegerField(blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    room_code = models.CharField(max_length=50, blank=True, null=True)
    room_name = models.CharField(max_length=100, blank=True, null=True)
    scholar_year = models.IntegerField(blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scholar'


class ServiceHourListing(models.Model):
    serv_hours_id = models.IntegerField(primary_key=True)
    serv_hours_date = models.DateField(blank=True, null=True)
    serv_hours_time = models.TimeField(blank=True, null=True)
    serv_hours_loc = models.CharField(max_length=255, blank=True, null=True)
    serv_hours_slot_count = models.IntegerField(blank=True, null=True)
    serv_hours_task = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_hour_listing'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    user_password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'