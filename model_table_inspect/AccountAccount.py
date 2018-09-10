# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountAccount(models.Model):
    name = models.CharField(max_length=-1)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=64)
    deprecated = models.NullBooleanField()
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING)
    internal_type = models.CharField(max_length=-1, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    reconcile = models.NullBooleanField()
    note = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    group = models.ForeignKey('AccountGroup', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)
