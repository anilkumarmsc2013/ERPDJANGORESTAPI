# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountJournal(models.Model):
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=5)
    active = models.NullBooleanField()
    type = models.CharField(max_length=-1)
    default_credit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    default_debit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    update_posted = models.NullBooleanField()
    group_invoice_lines = models.NullBooleanField()
    sequence = models.ForeignKey('IrSequence', models.DO_NOTHING)
    refund_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    sequence_0 = models.IntegerField(db_column='sequence', blank=True, null=True)  # Field renamed because of name conflict.
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    refund_sequence_0 = models.NullBooleanField(db_column='refund_sequence')  # Field renamed because of name conflict.
    at_least_one_inbound = models.NullBooleanField()
    at_least_one_outbound = models.NullBooleanField()
    profit_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    loss_account = models.ForeignKey('AccountAccount', models.DO_NOTHING, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    bank_statements_source = models.CharField(max_length=-1, blank=True, null=True)
    show_on_dashboard = models.NullBooleanField()
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('code', 'name', 'company'),)
