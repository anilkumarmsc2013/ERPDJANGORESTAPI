# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountMove(models.Model):
    name = models.CharField(max_length=-1)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    state = models.CharField(max_length=-1)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    matched_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_cash_basis_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    stock_move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move'
