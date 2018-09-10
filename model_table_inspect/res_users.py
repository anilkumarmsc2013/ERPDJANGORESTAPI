# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ResUsers(models.Model):
    active = models.NullBooleanField()
    login = models.CharField(unique=True, max_length=-1)
    password = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    signature = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    share = models.NullBooleanField()
    create_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    password_crypt = models.CharField(max_length=-1, blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, blank=True, null=True)
    notification_type = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'res_users'
