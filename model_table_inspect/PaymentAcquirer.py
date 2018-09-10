# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class PaymentAcquirer(models.Model):
    name = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    provider = models.CharField(max_length=-1)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    view_template = models.ForeignKey('IrUiView', models.DO_NOTHING)
    registration_view_template = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    environment = models.CharField(max_length=-1)
    website_published = models.NullBooleanField()
    capture_manually = models.NullBooleanField()
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    specific_countries = models.NullBooleanField()
    pre_msg = models.TextField(blank=True, null=True)
    post_msg = models.TextField(blank=True, null=True)
    pending_msg = models.TextField(blank=True, null=True)
    done_msg = models.TextField(blank=True, null=True)
    cancel_msg = models.TextField(blank=True, null=True)
    error_msg = models.TextField(blank=True, null=True)
    save_token = models.CharField(max_length=-1, blank=True, null=True)
    fees_active = models.NullBooleanField()
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, blank=True, null=True)
    payment_flow = models.CharField(max_length=-1)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_acquirer'
