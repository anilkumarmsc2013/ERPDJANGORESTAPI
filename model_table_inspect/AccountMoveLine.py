# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccountMoveLine(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom = models.ForeignKey('ProductUom', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_cash_basis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    account = models.ForeignKey('AccountAccount', models.DO_NOTHING)
    move = models.ForeignKey('AccountMove', models.DO_NOTHING)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey('AccountBankStatementLine', models.DO_NOTHING, blank=True, null=True)
    statement = models.ForeignKey('AccountBankStatement', models.DO_NOTHING, blank=True, null=True)
    reconciled = models.NullBooleanField()
    full_reconcile = models.ForeignKey('AccountFullReconcile', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    blocked = models.NullBooleanField()
    date_maturity = models.DateField()
    date = models.DateField(blank=True, null=True)
    tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey('AccountAnalyticAccount', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user_type = models.ForeignKey('AccountAccountType', models.DO_NOTHING, blank=True, null=True)
    tax_exigible = models.NullBooleanField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    stored_invoice = models.ForeignKey('AccountInvoice', models.DO_NOTHING, blank=True, null=True)
    invoice_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'
