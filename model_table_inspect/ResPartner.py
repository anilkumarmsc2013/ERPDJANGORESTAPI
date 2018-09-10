# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class ResPartner(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    display_name = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    tz = models.CharField(max_length=-1, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    vat = models.CharField(max_length=-1, blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    active = models.NullBooleanField()
    customer = models.NullBooleanField()
    supplier = models.NullBooleanField()
    employee = models.NullBooleanField()
    function = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile = models.CharField(max_length=-1, blank=True, null=True)
    is_company = models.NullBooleanField()
    industry = models.ForeignKey('ResPartnerIndustry', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    partner_share = models.NullBooleanField()
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    commercial_partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    commercial_company_name = models.CharField(max_length=-1, blank=True, null=True)
    company_name = models.CharField(max_length=-1, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    activity_date_deadline = models.DateField(blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    opt_out = models.NullBooleanField()
    signup_token = models.CharField(max_length=-1, blank=True, null=True)
    signup_type = models.CharField(max_length=-1, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    invoice_warn = models.CharField(max_length=-1)
    invoice_warn_msg = models.TextField(blank=True, null=True)
    picking_warn = models.CharField(max_length=-1)
    picking_warn_msg = models.TextField(blank=True, null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'
