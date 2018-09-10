# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class PaymentTransaction(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    date_validate = models.DateTimeField(blank=True, null=True)
    acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING)
    type = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    state_message = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    reference = models.CharField(max_length=-1)
    acquirer_reference = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    partner_lang = models.CharField(max_length=-1, blank=True, null=True)
    partner_email = models.CharField(max_length=-1, blank=True, null=True)
    partner_zip = models.CharField(max_length=-1, blank=True, null=True)
    partner_address = models.CharField(max_length=-1, blank=True, null=True)
    partner_city = models.CharField(max_length=-1, blank=True, null=True)
    partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    partner_phone = models.CharField(max_length=-1, blank=True, null=True)
    html_3ds = models.CharField(max_length=-1, blank=True, null=True)
    callback_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    callback_res_id = models.IntegerField(blank=True, null=True)
    callback_method = models.CharField(max_length=-1, blank=True, null=True)
    callback_hash = models.CharField(max_length=-1, blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction'
