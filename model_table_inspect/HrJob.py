# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class HrJob(models.Model):
    name = models.CharField(max_length=-1)
    expected_employees = models.IntegerField(blank=True, null=True)
    no_of_employee = models.IntegerField(blank=True, null=True)
    no_of_recruitment = models.IntegerField(blank=True, null=True)
    no_of_hired_employee = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    message_last_post = models.DateTimeField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    hr_responsible = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING)
    color = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_job'
        unique_together = (('name', 'company', 'department'),)
