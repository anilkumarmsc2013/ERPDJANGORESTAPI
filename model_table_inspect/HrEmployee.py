# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class HrEmployee(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.NullBooleanField()
    address_home = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    gender = models.CharField(max_length=-1, blank=True, null=True)
    marital = models.CharField(max_length=-1, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    ssnid = models.CharField(max_length=-1, blank=True, null=True)
    sinid = models.CharField(max_length=-1, blank=True, null=True)
    identification_id = models.CharField(max_length=-1, blank=True, null=True)
    passport_id = models.CharField(max_length=-1, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    permit_no = models.CharField(max_length=-1, blank=True, null=True)
    visa_no = models.CharField(max_length=-1, blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    work_phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile_phone = models.CharField(max_length=-1, blank=True, null=True)
    work_email = models.CharField(max_length=-1, blank=True, null=True)
    work_location = models.CharField(max_length=-1, blank=True, null=True)
    job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    coach = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING)
    message_last_post = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee'
