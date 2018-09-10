# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class SaleOrder(models.Model):
    name = models.CharField(max_length=-1)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    client_order_ref = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    date_order = models.DateTimeField()
    validity_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    confirmation_date = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    partner_invoice = models.ForeignKey('ResPartner', models.DO_NOTHING)
    partner_shipping = models.ForeignKey('ResPartner', models.DO_NOTHING)
    pricelist = models.ForeignKey('ProductPricelist', models.DO_NOTHING)
    analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING, blank=True, null=True)
    invoice_status = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey('AccountFiscalPosition', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    activity_date_deadline = models.DateField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_tx = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True)
    payment_acquirer = models.ForeignKey('PaymentAcquirer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order'
