# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountPayment(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    payment_type = models.CharField(max_length=-1)
    payment_reference = models.CharField(max_length=-1, blank=True, null=True)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    destination_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    payment_difference_handling = models.CharField(max_length=-1, blank=True, null=True)
    writeoff_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    writeoff_label = models.CharField(max_length=-1, blank=True, null=True)
    message_last_post = models.DateTimeField(blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING)
    partner_type = models.CharField(max_length=-1, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    payment_date = models.DateField()
    communication = models.CharField(max_length=-1, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment'
