# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
